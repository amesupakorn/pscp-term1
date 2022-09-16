""" [Recommend] Diginity """

def loop(num):
    """ [Recommend] Diginity """
    total = 0
    for i in num:
        total += int(i)
    if len(str(total)) != 1:
        total = loop(str(total))
    return total
def main():
    """ [Midterm] Diginity """
    while True:
        num = input()
        ans = 0
        if num == "0":
            break
        else:
            ans = loop(num)
            print(ans)
main()
