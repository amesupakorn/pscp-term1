""" Sequence VIII """

def main(num):
    """ Sequence VIII """
    for i in range(1, num+1):
        for _ in range(num-i):
            print("  ", end=" ")
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        print()
main(int(input()))
