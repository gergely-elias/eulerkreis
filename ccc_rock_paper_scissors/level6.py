def replace_Xs(styles, M):
    pairing = ""
    for style in styles:
        if style == "X":
            pairing += "S"
        else:
            pairing += style
    return pairing
