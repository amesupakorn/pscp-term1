""" ProgressiveTax """

def main(money):
    """ ProgressiveTax """
    total = 0
    if money > 4000000:
        total += (money - 4000000) * 0.35 #หาว่า ต้องจ่ายภาษีเพิ่มเท่าไร
        money -= (money - 4000000) #ทำการหักลบภาษีรอบนี้ เพื่อไปคิดรอบต่อไป
    if money > 2000000:
        total += (money - 2000000) * 0.30
        money -= (money - 2000000)
    if money > 1000000:
        total += (money - 1000000) * 0.25
        money -= (money - 1000000)
    if money > 750000:
        total += (money - 750000) * 0.2
        money -= (money - 750000)
    if money > 500000:
        total += (money - 500000) * 0.15
        money -= (money - 500000)
    if money > 300000:
        total += (money - 300000) * 0.1
        money -= (money - 300000)
    if money > 150000:
        total += (money - 150000) * 0.05
        money -= (money - 150000)
    print("%d" %total)
main(int(input()))
