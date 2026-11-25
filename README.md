# Clinical Screening Benchmarks

Independent benchmark suite and experimental logs for non-invasive ocular screening models.

## Modules
- `src/metrics.py`: Standardized regression (MAE, RMSE) and classification metrics.
- `src/roc_curve.py`: ROC curve coordinates and trapezoidal AUC calculator.
- `src/cross_validation.py`: Leakage-free subject-aware partition generator.
- `src/logger.py`: JSON structured experiment run logger.
