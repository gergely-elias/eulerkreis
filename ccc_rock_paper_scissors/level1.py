def fight_winner(styles):
    strength_order = "RPS"
    strength_indices = [strength_order.index(style) for style in styles]
    strength_diff = (strength_indices[1] - strength_indices[0]) % len(strength_order)
    if strength_diff >= 0 and strength_diff < (len(strength_order) + 1) // 2:
        return styles[1]
    else:
        return styles[0]
