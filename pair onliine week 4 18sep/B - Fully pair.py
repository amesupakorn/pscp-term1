""" B - Fully pair? """

def main():
    """ B - Fully pair? """
    txt, ans = input(), ""
    for i in txt:
        amount = txt.count(i)
        if amount%2 == 0:
            txt = txt.replace(i, "")
            amount = 0
        else:
            txt = txt.replace(i, "")
            ans += i
    if ans == "":
        print("fully paired")
    else:
        print(ans)
main()
