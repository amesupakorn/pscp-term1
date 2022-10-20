"""MissingCard I"""
def main():
    """MissingCard I"""
    txt = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    card = []
    for i in txt:
        c_s = i + "S"
        c_h = i + "H"
        c_d = i + "D"
        c_c = i + "C"
        card.append(c_s)
        card.append(c_h)
        card.append(c_d)
        card.append(c_c)
    for _ in range(51):
        resemble = input()
        if resemble in card:
            card.remove(resemble)
    print(card[0])
main()
