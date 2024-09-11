import random

def replace_Xs_Z(styles, M):
    pairing = ""
    for style in styles:
        if style == "X":
            pairing += random.choice("RSPLY")
        else:
            pairing += style
    return pairing
