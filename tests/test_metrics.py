from src.metrics import compute_mae, compute_rmse

def test_regression_metrics():
    t = [12.0, 14.0, 10.5]
    p = [12.2, 13.8, 10.7]
    assert compute_mae(t, p) < 0.3
