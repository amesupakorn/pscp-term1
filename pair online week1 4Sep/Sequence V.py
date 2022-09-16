""" Sequence V """

def main(num):
    """ Sequence V """
    for i in range(0, num):
        if i % 7 == 0 and i != 0:
            print()
        print(num, end=" ")
        num -= 1
main(int(input()))
