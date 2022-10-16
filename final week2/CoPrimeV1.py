""" GCD_v1 """
def main(num1, num2):
    """ GCD_v1 """
    total = 1
    for i in range(1, num1+1):
        if num1 % i == 0 and num2 % i == 0:
            total = i
    if total == 1:
        print("YES")
        print(total)
    else:
        print("NO")
        print(total)
main(int(input()), int(input()))
