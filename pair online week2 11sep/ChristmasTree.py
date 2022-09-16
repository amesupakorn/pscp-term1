""" ChristmasTree """

def main():
    """ ChristmasTree """
    num = int(input())
    stick = int(input())
    for i in range(1, num + 1):
        print(" "*(num-i), end="")
        print("*"*(i*2-1))
    for _ in range(stick):
        print(" "*(num-2), end="")
        print("---")
main()
