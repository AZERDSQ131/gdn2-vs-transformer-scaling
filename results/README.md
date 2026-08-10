# Result files

`metrics.csv` contains the primary validation and systems measurements used by
the article. `recurrent_depth.csv` contains the separate diagnostic ablation
for reapplying the same GDN2 blocks.

Blank fields mean that the corresponding secondary measurement was not
recorded for that seed. They are not zeroes and must not be imputed when
computing summaries.

The `status` column is intentional:

- `confirmed`: the comparison met the current seed gate;
- `provisional`: the comparison is real but not yet replicated;
- `diagnostic`: useful ablation, not a headline model comparison.
