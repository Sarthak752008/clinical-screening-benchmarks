# Experiment 06: Focal Loss vs Weighted Cross-Entropy

On the imbalanced stye detection dataset:
- Standard Cross-Entropy: F1-score = 0.742
- Weighted Cross-Entropy (pos_weight=4.0): F1-score = 0.789
- Focal Loss (gamma=2.0, alpha=0.25): F1-score = 0.818
- **Conclusion:** Focal loss yields best minority class recall without inflating false positives.
