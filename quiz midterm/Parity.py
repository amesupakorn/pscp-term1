""" Parity """
def main():
    """ Parity """
    total = 0
    txt = input()
    num = input()
    for i in txt:
        if i == "1":
            total += 1
    if num == "Even":
        if total % 2 == 0:
            print(txt+"0")
        else:
            print(txt+"1")
    elif num == "Odd":
        if total % 2 != 0:
            print(txt+"0")
        else:
            print(txt+"1")
main()
