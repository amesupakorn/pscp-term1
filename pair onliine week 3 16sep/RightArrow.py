""" RightArrow """
def main():
    """ RightArrow """
    width, high = int(input()), int(input())
    total = high//2
    for i in range(high):
        if i < total:
            for _ in range(i):
                print(" ", end="")
        else:
            for _ in range(high-i-1):
                print(" ", end="")
        print("*"*width, end="")
        print()
main()
