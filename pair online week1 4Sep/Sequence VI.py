""" Sequence VI """

def main(num):
    """ Sequence VI """
    for j in range(1, num+1):
        for i in range(1, j+1):
            print(i, end=" ")
        print()
main(int(input()))
