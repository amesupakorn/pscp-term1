"""Saint Seiya"""
def main(punch_second, punch):
    """Saint Seiya"""
    ans = 0
    for i in range(2, punch_second+1, 2):
        if ans < punch:
            if i%6 == 0:
                ans += 1
            elif i%2 == 0:
                ans += 165
        else:
            ans += (punch_second+1-i)*12 #+1 รอบ cash หายไป
            break
    print(ans)
main(int(input()), int(input()))
