""" Netflix """
def package(premium, standard, basic, mobile, total):
    """ package """
    if premium > 0:
        print("Premium x %d" % premium)
    if standard > 0:
        print("Standard x %d"% standard*(standard > 0))
    if basic > 0:
        print("Basic x %d" % basic*(basic > 0))
    if mobile > 0:
        print("Mobile x %d" % mobile*(mobile > 0))
    print("Total = %d THB" % total)
def main():
    """ Netflix """
    number_screen, number_phone = int(input()), int(input())
    input() #ไม่สน
    input() #ไม่สน
    watch_tv, hds, ultra = input().lower(), input().lower(), input().lower()
    premium, standard, basic = 0, 0, 0
    mobile, total = 0, 0
    while number_screen > 0 or number_phone > 0:
        if (ultra == "yes" or hds == "yes" or watch_tv == "yes") \
            and (number_screen >= 3 or number_phone >= 3):
            total += 419
            premium += 1
            number_screen -= 4
            number_phone -= 4
        elif (hds == "yes" or watch_tv == "yes") \
            and (number_screen >= 2 or number_phone >= 2):
            total += 349
            standard += 1
            number_screen -= 2
            number_phone -= 2
        elif watch_tv == "yes" and ultra == "no" and hds == "no":
            total += 279
            basic += 1
            number_screen -= 1
            number_phone -= 1
        else:
            if ultra == "yes":
                total += 419
                premium += 1
                number_screen -= 4
                number_phone -= 4
            elif hds == "yes":
                total += 349
                standard += 1
                number_screen -= 2
                number_phone -= 2
            elif watch_tv == "yes":
                total += 279
                basic += 1
                number_screen -= 1
                number_phone -= 1
            else:
                total += 99
                mobile += 1
                number_screen -= 1
                number_phone -= 1
    package(premium, standard, basic, mobile, total)
main()
