"""Diamond I"""

def main():
    """Diamond I"""
    num_m, num_n = int(input()), int(input())
    group = []
    ans = []
    for _ in range(num_m):
        group.append(input().split())
    for i in range(num_n):
        total = 0
        for j in group:
            total += int(j[i])
        ans.append(total)
    print(max(ans))
main()
