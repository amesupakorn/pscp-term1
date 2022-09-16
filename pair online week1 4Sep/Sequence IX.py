""" Sequence IX """

def main(num):
    """ Sequence IX """
    for j in range(1, num+1):
        for i in range(1, (num+1)-j):
            print("   ", end="")
        for i in range(j):
            print("%02d"%(i+1), end=" ")
        for i in range(j, 1, -1):
            print("%02d"%(i-1), end=" ")
        print()
main(int(input()))
