# Changelog

All notable changes to the Clinical Screening Benchmarks suite are documented in this file.

## [v0.1.1] - 2026-11-25
### Added
- ROC-AUC coordinate generator with trapezoidal integration in `src/roc_curve.py`.
- Subject-aware K-Fold cross-validation partitioning in `src/cross_validation.py`.
- Comprehensive benchmark comparisons across mobile architectures.
- Command-line flags for dynamic classification decision threshold tuning.

### Refactored
- Optimized confusion matrix generation logic in `src/metrics.py`.
