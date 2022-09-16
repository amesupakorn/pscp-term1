"""  Hamburger """

def main():
    """ Hamburger """
    numup, numlo = int(input()), int(input())
    ans = numlo+numup
    print("|" *numup + "**" *ans + "|" *numlo)
main()
