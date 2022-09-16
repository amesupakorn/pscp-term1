""" Key """

def main(num):
    """ Key """
    total = 0
    for i in num:
        total += int(i)
    num2 = int(num[10:13])*10
    ans = total+num2
    if ans >= 10000:
        ans = str(ans)
        ans = ans[1:5]
        print(ans)
    elif ans < 1000:
        ans += 1000
        print(ans)
    else:
        print(ans)
main(input())
