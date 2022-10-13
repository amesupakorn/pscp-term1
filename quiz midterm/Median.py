""" Median """
import math
def main():
    """ Median """
    mid = 0
    count = int(input())
    group = []
    for _ in range(count):
        num = int(input())
        group.append(num)
    group.sort()
    if count % 2 == 0:
        mid = math.ceil(count/2)
        real_ans = (group[mid-1] + group[mid])/2
        print("%.1f" %(real_ans))
    elif count % 2 == 1:
        mid = math.ceil(count/2)
        print("%.1f" %(group[mid-1]))
main()
