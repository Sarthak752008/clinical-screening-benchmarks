from src.image_validator import validate_image_dimensions

def test_valid_square_dimensions():
    valid, _ = validate_image_dimensions(224, 224)
    assert valid is True

def test_reject_low_resolution():
    valid, reason = validate_image_dimensions(64, 64)
    assert valid is False
    assert "below minimum" in reason
