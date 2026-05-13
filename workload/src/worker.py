# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.

"""Placeholder Temporal worker entry point.

Replace this with real workflow and activity registration before deploying
to anything that matters. The charm wires environment variables through
`TWC_*`; read what you need from `os.environ` here.
"""

import os
import signal
import sys
import time


def _shutdown(signum, _frame):
    print(f"[customer-temporal-worker] received signal {signum}, exiting", flush=True)
    sys.exit(0)


def main() -> None:
    signal.signal(signal.SIGTERM, _shutdown)
    signal.signal(signal.SIGINT, _shutdown)

    host = os.environ.get("TWC_HOST", "<unset>")
    namespace = os.environ.get("TWC_NAMESPACE", "<unset>")
    queue = os.environ.get("TWC_QUEUE", "<unset>")
    print(
        f"[customer-temporal-worker] placeholder loop "
        f"host={host} namespace={namespace} queue={queue}",
        flush=True,
    )
    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
