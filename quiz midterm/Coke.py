""" Coke """
def main():
    """ Coke """
    price, every, new = int(input()), int(input()), int(input())
    want = int(input())
    count, ans = 0, 0
    if every == 0:
        print(price*want)
    else:
        for _ in range(want):
            if count != every:
                ans += price
                count += 1
            else:
                ans += new
                count = 1
        print(ans)
main()
