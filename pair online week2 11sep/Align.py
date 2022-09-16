""" Align """
def main():
    """ Align """
    size, fuc, text = int(input()), input(), input()
    if fuc == "left":
        print(text)
    elif fuc == "center":
        ans = size - len(text)
        if ans % 2 == 1:
            text = " " + text
        print(text.center(size))
    elif fuc == "right":
        print(text.rjust(size))
main()
