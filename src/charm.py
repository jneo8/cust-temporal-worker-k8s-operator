#!/usr/bin/env python3
# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.

"""Customer Temporal Worker charm.

Thin downstream consumer of the `temporal_worker` charm library. Adds a
`certificates` relation as the entry point for relation-driven environment
data.
"""

from charms.temporal_worker_k8s.v0.temporal_worker import TemporalWorker
from ops import CharmBase, main


class CustomerTemporalWorkerCharm(CharmBase):
    """Charm wrapping the reusable Temporal worker controller."""

    def __init__(self, *args):
        super().__init__(*args)
        self.worker = TemporalWorker(self, extra_environment=self._extra_env)
        self.framework.observe(
            self.on["certificates"].relation_changed, self.worker.update
        )
        self.framework.observe(
            self.on["certificates"].relation_broken, self.worker.update
        )

    def _extra_env(self, charm: CharmBase) -> dict[str, str]:
        """Return downstream-specific environment variables for the worker."""
        return {}


if __name__ == "__main__":  # pragma: nocover
    main.main(CustomerTemporalWorkerCharm)
