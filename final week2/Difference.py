"""Difference"""
def main():
    """Difference"""
    set_n = set()
    set_m = set()
    numn, numm = int(input()), int(input())
    for _ in range(numn):
        set_n.add(int(input()))
    for _ in range(numm):
        set_m.add(int(input()))
    num = set_n.difference(set_m)
    num = sorted(num)
    for i in num:
        print(i, end=" ")
main()
