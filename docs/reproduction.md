# Reproduction boundary

This repository documents and validates the public result tables. It does not
pretend that a few YAML files are a complete training environment.

## Safe public contents

The repository contains no credentials, no private hostnames, no raw data, no
checkpoints and no cluster orchestration. The CSV files contain only the
published measurements. The scripts validate their schema and compute summary
statistics without contacting external services.

## Upstream GDN2 dependency

The original experiment used the official Gated DeltaNet-2 implementation and
a pinned `flash-linear-attention` commit. Those components are not copied here.
Read [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) and the upstream
license before installing them. In particular, do not assume that this
repository's Apache-2.0 license applies to the upstream kernels or to derived
weights.

## Re-running the full training

The private project contains hardware-specific training code and data
preparation that are deliberately outside this public kit. A future public
training release should only be made after:

1. the 120M comparison is replicated;
2. the parameter budgets are tightened;
3. data licenses are audited for redistribution;
4. the upstream GDN2 license is checked for the intended use;
5. all machine-specific paths and secrets are removed.
