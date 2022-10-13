""" LineSorting """
def main():
    """ LineSorting """
    num = int(input())
    group = []
    for _ in range(num):
        group.append(input())
    group.sort(key=len)
    for i in group:
        print(i)
main()
