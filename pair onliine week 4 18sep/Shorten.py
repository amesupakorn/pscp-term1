""" Shorten """

def main():
    """ Shorten """
    numx1, numx2, result = 0, 1, ''
    run = True
    while True:
        num = int(input())
        if num == -1:
            if run:
                print()
            else:
                result += str(numx1 + numx2 - 1)
            break
        if run:
            run = False
            numx1 = num
        else:
            if numx1 + numx2 == num:
                if numx2 == 1:
                    result += str(numx1) + '-'
                numx2 += 1
            else:
                result += str(numx1 + numx2 - 1) + ', '
                numx1 = num
                numx2 = 1
    print(result)
main()
