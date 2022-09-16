""" [Recommend] Restaurant """

def main():
    """ [Recommend] Restaurant """
    firstprice, promo, discount = float(input()), float(input()), float(input())
    buymore = float(input())
    if firstprice >= promo:
        ans = firstprice*((100-discount)/100) - firstprice
    else:
        ans = 0
    if firstprice + buymore >= promo:
        buymore = (firstprice + buymore)*((100-discount)/100) - firstprice
    else:
        buymore = 0
    if (buymore - ans) < 0:
        print('Yes %.03f'% abs(buymore - ans))
    elif (buymore - ans) > 0:
        print('No %.03f'%(buymore - ans))
    elif (buymore - ans) == 0:
        print('Yes')
main()
