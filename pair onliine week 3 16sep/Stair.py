""" Stair """

def main():
    """ Stair """
    max_hight, floor = int(input()), int(input())
    able = True
    check, count = 0, 0
    for _ in range(1, floor+1):
        step = int(input())
        check += step
        if step > max_hight:
            able = False
        elif check == max_hight:
            count += 1
            check = 0
        elif check > max_hight:
            count += 1
            check = step
    if check > 0:
        count += 1
    if able == False:
        print("NO")
    else:
        print(count)
main()
