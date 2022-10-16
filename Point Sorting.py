""" Point Sorting """
def main(num):
    """ Point Sorting """
    for _ in range(num):
        next = int(input())
        count = []
        for _ in range(next):
            txt = input().split()
            group = []
            group.append(int(txt[0]))
            group.append(int(txt[1]))
            count.append(group)
        count.sort(reverse=True, key=lambda count: count[1])
        count.sort(key=lambda count: count[0]+count[1])
        for i in count:
            for j in i:
                print(j, end=" ")
            print()
main(int(input()))
