""" Calculator V2 """
def main():
    """ Calculator V2 """
    num = int(input())
    count = len(str(num))
    tap_num = 0
    if num == 1:
        print(1)
    else:
        for i in range(1, count):
            tap_num += int("9" * i)
        print(int(num) * (count + 1) - tap_num)
main()
