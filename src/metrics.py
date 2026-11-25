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

def compute_confusion_matrix(y_true, y_pred):
    """Generates a 2x2 confusion matrix dictionary from binary inputs."""
    tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
    tn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 0)
    fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
    fn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)
    return {'TP': tp, 'TN': tn, 'FP': fp, 'FN': fn}
