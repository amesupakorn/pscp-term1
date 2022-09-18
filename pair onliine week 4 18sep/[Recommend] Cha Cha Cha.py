""" [Recommend] Cha Cha Cha """
import math
def main(day):
    """ [Recommend] Cha Cha Cha """
    ans = 0
    if day <= 31:
        for _ in range(day):
            hour = math.ceil(float(input()))
            ans += hour*8720
    print(ans)
main(int(input()))
