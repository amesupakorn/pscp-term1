""" Run Length Encoding """

def main():
    """ Run Length Encoding """
    txt = input()
    textchecker = txt[0]
    total = 0
    ans = ""
    for i in range(len(txt)):
        if textchecker == txt[i]:
            total += 1
        else:
            ans += str(total)+txt[i-1]
            textchecker = txt[i]
            total = 1
    ans += str(total)+txt[-1]
    print(ans)
main()
