""" Coke V2 """
def main():
    """ Coke V2 """
    price, every, nprice = int(input()), int(input()), int(input())
    want = int(input())
    if every == 0:
        print(price * want)
    elif want == 0:
        print(0)
    else:
        num = want - 1
        stack = num // every
        num2 = num % every
        print(price + (((price * (every - 1)) + nprice) * stack) + (price * num2))
main()
