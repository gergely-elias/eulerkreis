from level1 import fight_winner

def styles_after_two_rounds(styles, M):
    for round in range(2):
        matches = [styles[i:i+2] for i in range(0,M,2)]
        styles = "".join(map(fight_winner, matches))
        M = M // 2
    return styles
