""" Inflation """

def main(num):
    """ Inflation """
    for _ in range(int(input())):
        num += num*381//10000
    print("%d.%02d" % (num//100, num%100))
main(int(float(input())*100))
