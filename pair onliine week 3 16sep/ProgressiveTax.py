""" ProgressiveTax """

def main(money):
    """ ProgressiveTax """
    if money <= 150000:
        print(0)
    elif money <= 300000:
        print(int(((money - 150000)*0.05)))
    elif money <= 500000:
        print(int(((money - 300000)*0.10)) + 7500)
    elif money <= 750000:
        print(int(((money - 500000)*0.15)) + 27500)
    elif money <= 1000000:
        print(int(((money - 750000)*0.2)) + 65000)
    elif money <= 2000000:
        print(int(((money - 1000000)*0.25)) + 115000)
    elif money <= 4000000:
        print(int(((money - 2000000)*0.3)) + 365000)
    else:
        print(int(((money - 4000000)*0.35)) + 965000)
main(int(input()))
