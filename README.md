# GDN2 vs Transformer: scaling-regime reproduction kit

This repository accompanies the Substrate Research article:

**[GDN2 gagne petit. Un premier run suggère une inversion à l’échelle.](https://github.com/AZERDSQ131/G-serie/blob/main/site/articles/gdn2-vs-transformer.html)**

It contains the public, non-sensitive part of the experiment comparing a flat
Gated DeltaNet-2 model with a dense Transformer at two scales:

- approximately 30M parameters and 100M training tokens;
- approximately 120M parameters and 400M training tokens.

The repository is intentionally a **reproduction and analysis kit**, not a
copy of the private training environment. It includes:

- the published protocol and configuration summaries;
- seed-level and aggregate result tables;
- validation and aggregation scripts;
- a small plotting utility;
- notes about the upstream GDN2 dependency and its license.

It does **not** include checkpoints, raw training data, private machine paths,
credentials, cluster scripts, or a vendored copy of the upstream GDN2 kernels.

## Current status

The approximately 30M result is confirmed across three seeds: GDN2 flat has a
mean validation loss of `4.4238 ± 0.0267`, versus `4.5881 ± 0.0085` for the
Transformer.

The approximately 120M result currently has one seed. It favors the
Transformer (`1.9330` vs `2.1790` validation loss), but the replication is not
complete. That result is therefore published as provisional.

## Quick start

```bash
python3 scripts/validate_results.py
python3 -m unittest discover -s tests -v
python3 scripts/plot_results.py --output-dir /tmp/gdn2-scaling-plots
```

The plotting command requires `matplotlib`; the validation command uses only
the Python standard library.

## Reproduction boundary

The full CUDA training implementation is not copied here. GDN2 must be
obtained from the official upstream project and used under its own terms. See
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and
[`docs/reproduction.md`](docs/reproduction.md) before attempting a training
run.

## License

Original code and documentation in this repository are Apache-2.0 licensed.
Third-party components remain under their original licenses; they are not
relicensed by this repository.
