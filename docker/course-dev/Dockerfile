FROM maven:3.9.9-eclipse-temurin-17

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip curl bash \
    && python3 -m pip install --no-cache-dir --break-system-packages elasticsearch==8.18.0 cryptography==44.0.2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

CMD ["bash", "-lc", "sleep infinity"]
