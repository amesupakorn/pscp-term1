"""Runner"""
def main():
    """Runner"""
    distance = float(input())
    num = int(input())
    lst = []
    run = []
    for _ in range(num):
        lst.append(input().split(" "))
    lst2 = lst.copy()
    lst.sort(key=lambda i: float(i[0]), reverse=True)
    for i in lst:
        run.append((distance-float(i[1]))/float(i[0]))
    print(lst2.index(lst[run.index(min(run))])+1)
main()
