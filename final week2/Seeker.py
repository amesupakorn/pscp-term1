""" Seeker """
def main():
    """ Seeker """
    txt, check = input(), ""
    ans = 0
    for i in txt:
        if i.isdigit() == True:
            check += i
        else:
            if check == "":
                ans += 0
            else:
                ans += int(check)
                check = ""
    if check.isdigit() == True:
        print(ans + int(check))
    else:
        print(ans)
main()
