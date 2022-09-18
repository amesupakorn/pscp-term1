""" snacks """

def main():
    """ snacks """
    top, snack, down = input(), input(), input()
    num = int(input())
    eat_count = 0
    left_count = 0
    eat = snack[:num:]
    left = snack[num::]
    for i in eat:
        if i == ")":
            eat_count += 1
    for i in left:
        if i == ")":
            left_count += 1
    print(eat_count)
    if left_count == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(top)
    print("%s%s" %((" "*num), snack[num:]))
    print(down)
main()
