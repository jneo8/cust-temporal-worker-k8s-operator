# customer-temporal-worker-operator

> **Prototype.** Not for production use. This repository exists to validate
> the `temporal_worker` charm-library refactor end-to-end by building a real
> downstream consumer, and to serve as a reference for teams creating their
> own customer Temporal worker charms.

A customer-owned Kubernetes charm that runs Temporal workflow and activity
code. The charm itself is a thin wrapper around the upstream(fork)
[`temporal_worker`](https://github.com/jneo8/temporal-worker-k8s-operator/tree/refactor/temporal-worker-lib)
charm library — all reconcile, relation, and workload-management logic lives
in the library. This repo contributes:

- a thin `src/charm.py` that instantiates the library and hooks in any
  customer-specific environment or relations
- a workload [rock](https://documentation.ubuntu.com/rockcraft/) carrying
  the customer's workflow code
- charm metadata, configuration, and resource declarations
