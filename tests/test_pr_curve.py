from src.pr_curve import compute_pr_curve

def test_pr_curve_bounds():
    y_true = [1, 1, 0, 1, 0, 0]
    scores = [0.9, 0.85, 0.4, 0.75, 0.2, 0.1]
    p, r, ap = compute_pr_curve(y_true, scores)
    assert 0.0 <= ap <= 1.0
    assert len(p) == len(r)
    assert all(0.0 <= x <= 1.0 for x in p)
