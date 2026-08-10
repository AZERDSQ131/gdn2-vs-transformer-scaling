# Experimental protocol

## Question

Does a flat Gated DeltaNet-2 model retain a validation-loss or systems
advantage over a dense Transformer when the experiment moves from an
ultra-compact regime to an approximately 120M-parameter regime?

## Controlled variables

- same tokenizer;
- same repository-disjoint train/validation split;
- same sequence length: 2048 tokens;
- same FIM rate: 0.5;
- same effective batch: `32 x 4`;
- same warmup + cosine schedule;
- same number of training tokens within each scale;
- seeds fixed before inspecting the result.

## Measurements

The primary metric is final validation loss. Secondary metrics are perplexity,
approximate FLOPs/token, training throughput and peak memory. These metrics
must not be collapsed into a single score: theoretical FLOPs and real tokens/s
answer different questions.

## Scale caveat

The 30M models are close in size but not identical: 29.92M versus 32.51M
parameters. The 120M models are less closely matched: 108.38M versus 125.72M.
The 120M comparison must therefore be described as a comparison at a similar
scale, not as a strict parameter-matched experiment.

## Current evidence gate

- 30M: confirmed across seeds 1337, 1338 and 1339.
- 120M: provisional, seed 1337 only.
- 120M publication-quality conclusion: requires at least two additional seeds
  and a check that the parameter mismatch does not explain the inversion.
