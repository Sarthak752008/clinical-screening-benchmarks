def compute_mae(y_true, y_pred):
    return sum(abs(a - b) for a, b in zip(y_true, y_pred)) / len(y_true)

def compute_rmse(y_true, y_pred):
    return (sum((a - b)**2 for a, b in zip(y_true, y_pred)) / len(y_true)) ** 0.5
