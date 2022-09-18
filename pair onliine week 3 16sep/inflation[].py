"""Inflation"""
def main():
    """Inflation"""
    cost = float(input())
    years = int(input())
    percent = 381
    cost = int(cost * 100)
    for _ in range(years):
        interest = cost * percent
        cost += interest// 10000
    ans1 = str(cost) #105642345643246544654658318
    ans2 = ans1[-2::]
    ans3 = ans1[::-1] #813016544654654654654
    ans3 = ans3[2::] #3016456456465465
    ans3 = ans3[::-1] #
    if ans3 == "":
        ans3 = "0"
    if ans2 == "":
        ans2 = "0"
    print("%d.%02d"%(int(ans3), int(ans2)))
main()
