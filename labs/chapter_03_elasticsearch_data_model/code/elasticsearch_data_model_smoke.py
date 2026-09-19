"""Load the supplied product data into a disposable Elasticsearch index."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE = os.environ.get("ELASTICSEARCH_URL", "http://localhost:9200").rstrip("/")
INDEX = "course_products_example"
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "products.json"


def request(method: str, path: str, body: object | None = None) -> dict:
    payload = None if body is None else json.dumps(body).encode("utf-8")
    headers = {"Accept": "application/json"}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    with urlopen(Request(BASE + path, data=payload, headers=headers, method=method), timeout=15) as response:
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
    try:
        health = wait_for_service()
        request("PUT", f"/{INDEX}")
        bulk = DATA_FILE.read_text(encoding="utf-8").rstrip("\n") + "\n"
        with urlopen(
            Request(
                BASE + f"/{INDEX}/_bulk",
                data=bulk.encode("utf-8"),
                headers={"Content-Type": "application/x-ndjson"},
                method="POST",
            ),
            timeout=15,
        ) as response:
            result = json.loads(response.read().decode("utf-8"))
        if result.get("errors"):
            raise RuntimeError("bulk load returned errors")

        request("POST", f"/{INDEX}/_refresh")
        count = request("GET", f"/{INDEX}/_count")
        match = request("GET", f"/{INDEX}/_search", {"query": {"match": {"name": "Apple"}}})
        phrase = request(
            "GET",
            f"/{INDEX}/_search",
            {"query": {"match_phrase": {"name": "Apple IPhone 13"}}},
        )
        if count.get("count") != 5 or not match.get("hits", {}).get("hits") or not phrase.get("hits", {}).get("hits"):
            raise RuntimeError("the supplied product queries did not return the expected results")
        print("ELASTICSEARCH EXAMPLE PASSED")
        print(f"cluster_status={health.get('status')} count={count.get('count')}")
        return 0
    except (HTTPError, URLError, OSError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"ELASTICSEARCH EXAMPLE FAILED: {exc}", file=sys.stderr)
        return 1
    finally:
        try:
            request("DELETE", f"/{INDEX}")
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
