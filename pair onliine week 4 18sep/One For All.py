""" One For All """

def main():
    """ One For All """
    total = int(input())
    num = 0
    ans = ""
    for _ in range(total):
        txt = input()
        num += 1
        if num == total:
            ans += (txt+"_%d"%total)
        elif num % 2 == 0:
            ans += (txt+"-"*num)
        else:
            ans += (txt+"*"*num)
    print(ans)
main()
