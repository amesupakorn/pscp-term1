""" RockPaperScissor """

def main():
    """ RockPaperScissor """
    txt = input()
    if playera(txt) > playerb(txt):
        print("A win %d-%d" %(playera(txt), playerb(txt)))
    if playera(txt) < playerb(txt):
        print("B win %d-%d" %(playerb(txt), playera(txt)))
    if playera(txt) == playerb(txt):
        print("DRAW %d" %(playera(txt)))
def playerb(txt):
    """ b """
    player_b = 0
    for i in range(0, len(txt), 2):
        unknow = (txt[i:i+2])
        if unknow == "SR":
            player_b += 1
        elif unknow == "RP":
            player_b += 1
        elif unknow == "PS":
            player_b += 1
        elif unknow == "SS" or unknow == "PP" or unknow == "RR":
            player_b += 0
    return player_b
def playera(txt):
    """ a """
    player_a = 0
    for i in range(0, len(txt), 2):
        unknow = (txt[i:i+2])
        if unknow == "RS":
            player_a += 1
        elif unknow == "PR":
            player_a += 1
        elif unknow == "SP":
            player_a += 1
        elif unknow == "SS" or unknow == "PP" or unknow == "RR":
            player_a += 0
    return player_a
main()
