""" Tuple's Sad life """
def main():
    """ Tuple's Sad life """
    txt = input().split()
    num = input()
    loca = 0
    amout = txt.count(num)
    loca = int(txt.index(num))
    for _ in range(amout):
        for _ in range(amout):
            print(loca, end=" ")
        print()
main()
