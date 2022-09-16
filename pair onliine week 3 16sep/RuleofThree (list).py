""" RuleofThree """
def main(num):
    """ RuleofThree """
    mylist = []
    get = 0
    for _ in range(num):
        prince = float(input())
        weight = float(input())
        if mylist == []:
            mylist.append(prince)
            mylist.append(weight)
            get = weight/prince
        if get > weight/prince and get != 0:
            continue
        elif get < weight/prince and get != 0:
            get = weight/prince
            mylist.clear()
            mylist.append(prince)
            mylist.append(weight)
        elif get == weight/prince and get != 0:
            if mylist[0] > prince:
                mylist.clear()
                mylist.append(prince)
                mylist.append(weight)
    print("%.2f %.2f"%(mylist[0], mylist[1]))
main(int(input()))
