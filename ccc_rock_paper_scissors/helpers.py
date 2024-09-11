from level1 import fight_winner

def tourney_winner(styles, M):
    while M > 1:
        matches = [styles[i:i+2] for i in range(0,M,2)]
        styles = "".join(map(fight_winner, matches))
        M = M // 2
    return styles

def fight_winner_5(styles):
    strength_order = "RYPLS"
    strength_indices = [strength_order.index(style) for style in styles]
    strength_diff = (strength_indices[1] - strength_indices[0]) % len(strength_order)
    if strength_diff >= 0 and strength_diff < (len(strength_order) + 1) // 2:
        return styles[1]
    else:
        return styles[0]

def tourney_winner_5(styles, M):
    while M > 1:
        matches = [styles[i:i+2] for i in range(0,M,2)]
        styles = "".join(map(fight_winner_5, matches))
        M = M // 2
    return styles

def fight_winner_5_Z(styles):
    s1, s2 = styles
    # print(s1, s2)
    s = set({})
    for ss1 in s1:
        for ss2 in s2:
            s.add(fight_winner_5(ss1 + ss2))
    # strength_order = "RYPLS"
    # strength_indices = [strength_order.index(style) for style in styles]
    # strength_diff = (strength_indices[1] - strength_indices[0]) % len(strength_order)
    # if strength_diff >= 0 and strength_diff < (len(strength_order) + 1) // 2:
    #     return styles[1]
    # else:
    #     return styles[0]
    return list(s)

def tourney_winner_5_Z(styles, M):
    styles_as_lists = [["R", "Y", "P", "L", "S"] if style == "Z" else [style] for style in styles]
    # print(styles_as_lists)
    while M > 1:
        # print(M)
        # matches = [styles_as_lists[i:i+2] for i in range(0,M,2)]
        next_round_styles_as_lists = []
        for i in range(0,M,2):
            next_round_styles_as_lists.append(fight_winner_5_Z(styles_as_lists[i:i+2]))
        # styles_as_lists = [].extend(map(fight_winner_5_Z, matches))
        M = M // 2
        styles_as_lists = next_round_styles_as_lists
    return styles_as_lists[0]
