"""BusStop I"""
def main():
    """BusStop I"""
    amount = int(input())
    count = int(input())
    group = []
    groupincar = []
    ans = 0
    for _ in range(count):
        bus = input().split()
        group.append(bus)
    group.sort(key=lambda i: int(i[0]))
    for i in group:
        stop = int(i[0])# รถหยุด
        #remove
        if len(groupincar) != 0:
            groupincar2 = groupincar.copy()
            for arrive in groupincar:
                if arrive == stop:
                    groupincar2.remove(arrive)
                    ans += 1
            groupincar = groupincar2
        for j in range(1, len(i)):
            if len(groupincar) == amount:
                break
            if stop < int(i[j]):
                groupincar.append(int(i[j]))
    print(ans)
main()
