""" Parallelogram """

def main(txt):
    """ Parallelogram """
    total = len(txt)
    for i in range(0, total):
        print(" "*(total-i-1)+txt[0:i+1])
    for j in range(0, total):
        print(txt[j+1:total:])
main(input())
