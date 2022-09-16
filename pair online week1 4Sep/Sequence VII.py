""" Sequence VII """

def main(num):
    """ Sequence VII """
    for i in range(1, num+1):
        for j in range(i):
            print(j+1, end=" ")
        print()
    for i in range(num-1, 0, -1):
        for j in range(i):
            print(j+1, end=" ")
        print()
main(int(input()))
