from src.calibration import compute_ece

def test_ece_bounds():
    val = compute_ece([], [], [])
    assert 0.0 <= val <= 1.0
