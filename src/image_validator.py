"""Pre-ingestion image sanity and aspect ratio validation utility."""

def validate_image_dimensions(width, height, min_res=128, max_aspect_ratio=2.5):
    if width < min_res or height < min_res:
        return False, "Resolution below minimum screening threshold"
    aspect = max(width, height) / max(min(width, height), 1)
    if aspect > max_aspect_ratio:
        return False, f"Extreme aspect ratio {aspect:.2f} exceeds threshold"
    return True, "Valid"
