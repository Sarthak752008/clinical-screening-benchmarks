from src.roc_curve import compute_roc_coordinates

def test_perfect_classifier_auc():
    y_true = [1, 1, 0, 0]
    scores = [0.9, 0.8, 0.2, 0.1]
    _, _, auc = compute_roc_coordinates(y_true, scores)
    assert auc >= 0.95

def test_auc_within_unit_interval():
    y_true = [1, 0, 1, 0]
    scores = [0.6, 0.4, 0.3, 0.7]
    _, _, auc = compute_roc_coordinates(y_true, scores)
    assert 0.0 <= auc <= 1.0
