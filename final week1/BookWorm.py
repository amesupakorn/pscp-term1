"""bookworm"""

def main():
    """bookworm"""
    for _ in range(int(input())):
        minute = float(input())
        group = sorted([float(input()) for _ in range(int(input()))])
        total = 0
        ans = 0
        for i in range(len(group)):
            total += group[i]
            if total <= minute:
                ans += 1
        print(ans)
main()
