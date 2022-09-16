""" Bill """

def main(bill):
    """ Bill """
    service = bill*0.1
    if service < 50:
        service = 50
    if service > 1000:
        service = 1000
    vat = (bill + service)* 0.07
    print("%.2f" %(bill + service + vat))
main(float(input()))
