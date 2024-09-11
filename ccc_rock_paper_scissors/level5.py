def first_round_pairing_whole_tourney_5(style_counts, M):
    pairing = ""
    for style in "RYPLS":
        pairing += style * style_counts[style]
    return pairing
