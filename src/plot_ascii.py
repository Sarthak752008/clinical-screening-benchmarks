"""Terminal ASCII visualization helper for metric curves."""

def render_ascii_curve(x_vals, y_vals, width=40, height=12):
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    for x, y in zip(x_vals, y_vals):
        gx = min(int(x * (width - 1)), width - 1)
        gy = min(int((1.0 - y) * (height - 1)), height - 1)
        grid[gy][gx] = '*'
    lines = [''.join(row) for row in grid]
    return '\n'.join(lines)
