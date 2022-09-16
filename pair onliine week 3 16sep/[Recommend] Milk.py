""" [Recommend] Milk """

def main():
    """ [Recommend] Milk """
    price, every, free = int(input()), int(input()), int(input())
    money = int(input())
    ans = money//price
    bottle = ans
    while bottle >= every and every != 0:
        get_free = (bottle // every) * free
        ans += get_free
        bottle -= (bottle // every) * every
        bottle += get_free
    print(ans)
main()
