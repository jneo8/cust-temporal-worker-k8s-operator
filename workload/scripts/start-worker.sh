#!/bin/bash
# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.

set -eu

echo "[customer-temporal-worker] starting placeholder worker"
env | grep -E '^TWC_' | sort || true

exec python3 /app/src/worker.py
