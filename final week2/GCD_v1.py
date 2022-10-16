""" GCD_v1 """
def main(num1, num2):
    """ GCD_v1 """
    total = 100000
    while True:
        total -= 1
        if num1 % total == 0 and num2 % total == 0:
            print(total)
            break
main(int(input()), int(input()))