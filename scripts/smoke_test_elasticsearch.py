"""Run the supplied Elasticsearch product operations against a disposable index."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
BASE = os.environ.get("ELASTICSEARCH_URL", "http://localhost:9200").rstrip("/")
INDEX = "workbook_products_smoke"


def request(method: str, path: str, body: object | None = None) -> dict:
    payload = None
    headers = {"Accept": "application/json"}
    if body is not None:
        payload = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(BASE + path, data=payload, headers=headers, method=method)
    with urlopen(req, timeout=15) as response:
        raw = response.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def wait_for_service() -> dict:
    last_error: Exception | None = None
    for _ in range(30):
        try:
            health = request("GET", "/_cluster/health")
            if health.get("status") in {"green", "yellow"}:
                return health
        except (HTTPError, URLError, OSError, json.JSONDecodeError) as exc:
            last_error = exc
        time.sleep(2)
    raise RuntimeError(f"Elasticsearch did not become ready: {last_error}")


def main() -> int:
    products = Path(
        os.environ.get(
            "ELASTICSEARCH_PRODUCTS",
            str(ROOT / "workbooks/03_elasticsearch/products.json"),
        )
    )
    if not products.is_file():
        raise FileNotFoundError(f"supplied product data file not found: {products}")
    try:
        health = wait_for_service()

        request("PUT", f"/{INDEX}")
        bulk = products.read_text(encoding="utf-8")
        req = Request(
            BASE + f"/{INDEX}/_bulk",
            data=(bulk.rstrip("\n") + "\n").encode("utf-8"),
            headers={"Content-Type": "application/x-ndjson"},
            method="POST",
        )
        with urlopen(req, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))
        if result.get("errors"):
            raise RuntimeError(f"bulk load returned errors: {result}")

        request("POST", f"/{INDEX}/_refresh")
        count = request("GET", f"/{INDEX}/_count")
        if count.get("count") != 5:
            raise RuntimeError(f"expected five supplied products, got {count}")

        match = request("GET", f"/{INDEX}/_search", {"query": {"match": {"name": "Apple"}}})
        if not match.get("hits", {}).get("hits"):
            raise RuntimeError("match query returned no Apple product")

        phrase = request(
            "GET",
            f"/{INDEX}/_search",
            {"query": {"match_phrase": {"name": "Apple IPhone 13"}}},
        )
        if not phrase.get("hits", {}).get("hits"):
            raise RuntimeError("phrase query returned no supplied iPhone product")

        print("ELASTICSEARCH SMOKE TEST PASSED")
        print(f"cluster_status={health.get('status')} count={count.get('count')}")
        return 0
    except (HTTPError, URLError, OSError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"ELASTICSEARCH SMOKE TEST FAILED: {exc}", file=sys.stderr)
        return 1
    finally:
        try:
            request("DELETE", f"/{INDEX}")
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
