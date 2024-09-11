def first_round_pairing_whole_tourney(style_counts, M):
    pairing = ""
    for style in "RPS":
        pairing += style * style_counts[style]
    return pairing
