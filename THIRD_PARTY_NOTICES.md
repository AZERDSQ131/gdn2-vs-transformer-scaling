# Third-party notices

This repository does not vendor the Gated DeltaNet-2 implementation. The
training implementation used for the reported experiment came from the
official NVIDIA repository:

- Repository: <https://github.com/NVlabs/GatedDeltaNet-2>
- Paper: <https://arxiv.org/abs/2605.22791>
- License: NVIDIA Source Code License-NC
- Scope: research and evaluation only, according to the upstream license

The compatible `flash-linear-attention` dependency was pinned in the private
experiment to commit:

```text
4b02d15d6a68700181b180235be62a9fb95d2a38
```

Do not interpret this repository's Apache-2.0 license as relicensing NVIDIA
code or any other third-party dependency. Check the upstream license before
using the training implementation or publishing derived weights.
