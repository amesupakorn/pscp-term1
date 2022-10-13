"""Volleyball"""
def show(match, pointa, pointb, scorea, scoreb):
    """ match """
    if scorea == 3 or scoreb == 3:
        if scorea > scoreb:
            print("A won %d:%d set" %(scorea, scoreb))
        elif scoreb > scorea:
            print("B won %d:%d set" %(scoreb, scorea))
    else:
        print("Set %d: A (%d) | B (%d)" %(match, pointa, pointb))
        print("The game has not finished yet.")
def main():
    """ point """
    text = input()
    scorea, scoreb, pointa = 0, 0, 0
    pointb, match = 0, 1
    for i in text:
        if i == "A":
            pointa += 1
        elif i == "B":
            pointb += 1
        if match == 5:
            if pointa >= 15 or pointb >= 15:
                if pointa - 2 >= pointb:
                    scorea += 1
                    print("Set %d: A (%d) | B (%d)" %(match, pointa, pointb))
                elif pointb - 2 >= pointa:
                    scoreb += 1
                    print("Set %d: A (%d) | B (%d)" %(match, pointa, pointb))
        else:
            if pointa >= 25 or pointb >= 25:
                if pointa - 2 >= pointb:
                    scorea += 1
                    print("Set %d: A (%d) | B (%d)" %(match, pointa, pointb))
                    pointa, pointb = 0, 0
                    match += 1
                elif pointb - 2 >= pointa:
                    scoreb += 1
                    print("Set %d: A (%d) | B (%d)" %(match, pointa, pointb))
                    pointa, pointb = 0, 0
                    match += 1
    show(match, pointa, pointb, scorea, scoreb)
main()
