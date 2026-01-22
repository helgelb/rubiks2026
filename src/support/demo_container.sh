#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME=${IMAGE_NAME:-rubiks-demo}

docker build -t "$IMAGE_NAME" .
docker run --rm -v "$PWD/output:/app/output" "$IMAGE_NAME"
