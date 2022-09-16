""" Run Length Decoding """

def main():
    """ Run Length Decoding """
    text = input()
    text2 = ""
    for i in text:
        if i.isnumeric():
            text2 += i
        else:
            print(i*(int(text2)), end="")
            text2 = ""
main()
