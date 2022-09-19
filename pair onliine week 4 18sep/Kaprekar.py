""" Kaprekar """
def main():
    """ Kaprekar """
    num, count = str(input()), 0
    num2 = []
    realnum, realnum2 = "", ""
    while num != "6174":
        if int(num) < 1000:
            for i in num:
                num2.append(i)
            num2.insert(0, "0")
        else:
            for i in num:
                num2.append(i)
        sor(num2)
        newnum = num2[::-1]
        for i in num2:
            realnum += i
        for i in newnum:
            realnum2 += i
        num = int(realnum)-int(realnum2)
        count += 1
        num = str(num)
        num2 = []
        realnum = ""
        realnum2 = ""
    print(count)
def sor(num2):
    """ sor """
    if num2[0] <= num2[1]:
        num2[0], num2[1] = num2[1], num2[0]
    if num2[0] <= num2[2]:
        num2[0], num2[2] = num2[2], num2[0]
    if num2[0] <= num2[3]:
        num2[0], num2[3] = num2[3], num2[0]
    if num2[1] <= num2[2]:
        num2[1], num2[2] = num2[2], num2[1]
    if num2[1] <= num2[3]:
        num2[1], num2[3] = num2[3], num2[1]
    if num2[2] <= num2[3]:
        num2[2], num2[3] = num2[3], num2[2]
    return num2
main()
