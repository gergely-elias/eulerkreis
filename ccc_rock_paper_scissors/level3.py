from level1 import fight_winner

def first_round_pairing(style_counts, M):
    pairing = ""
    while style_counts["R"] > 2:
        pairing += "PRRR"
        style_counts["P"] -= 1
        style_counts["R"] -= 3
    pairing += "P" + "R" * style_counts["R"] + "P" * (style_counts["P"] - 1) + "S" * style_counts["S"]
    return pairing
