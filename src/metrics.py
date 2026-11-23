def compute_mae(y_true, y_pred):
    return sum(abs(a - b) for a, b in zip(y_true, y_pred)) / len(y_true)

def compute_rmse(y_true, y_pred):
    return (sum((a - b)**2 for a, b in zip(y_true, y_pred)) / len(y_true)) ** 0.5

def compute_sensitivity(tp, fn):
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0

def compute_specificity(tn, fp):
    return tn / (tn + fp) if (tn + fp) > 0 else 0.0

def safe_divide(numerator, denominator, fallback=0.0):
    return numerator / denominator if denominator != 0 else fallback
