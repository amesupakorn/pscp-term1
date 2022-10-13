"""Calculator"""

def main():
    """input"""
    num = int(input())
    count = 0
    if num == 1:
        print(1)
    else:
        for i in range(num):
            count += len(str(i+1))
            count += 1
        print(count)
main()
