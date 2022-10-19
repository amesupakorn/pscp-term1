""" Point Sorting """
def main(num):
    """ Point Sorting """
    for _ in range(num):
        count = []
        for _ in range(int(input())):
            txt = input().split()
            group = []
            group.extend([int(txt[0]), int(txt[1])])
            count.append(group)
        count.sort(reverse=True, key=lambda count: count[1])
        count.sort(key=lambda count: count[0] + count[1])
        for i in range(len(count)):
            print(*count[i])
main(int(input()))
