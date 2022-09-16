""" Sequence IV """

def main(num):
    """ Sequence IV """
    for i in range(1, (num*num)+1):
        print(i, end=" ")
        if i % num == 0:
            print()
main(int(input()))
