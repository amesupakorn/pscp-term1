"""Solar System"""
def main(txt):
    """Solar System"""
    lst_star, word = [], ""
    for i in txt:
        if i == " ":
            lst_star.insert(0, word)
            word = ""
        else:
            word += i
    lst_star.insert(0, word)
    lst_star = lst_star[::-1]
    ls1, lsl, lss = lst_star[0], lst_star[-1], lst_star.index("Sun")
    if ls1 == "Sun":
        print("Hot: "+lst_star[1])
        print("Cool: "+lsl)
    elif lsl == "Sun":
        print("Hot: "+lst_star[-2])
        print("Cool: "+ls1)
    else:
        print("Hot: %s %s"%(lst_star[lss-1], lst_star[lss+1]))
        if abs(lst_star.index(ls1)-lss) == abs(lst_star.index(lsl)-lss):
            print("Cool: %s %s"%(ls1, lsl))
        elif abs(lst_star.index(ls1)-lss) > abs(lst_star.index(lsl)-lss):
            print("Cool: %s"%ls1)
        elif abs(lst_star.index(ls1)-lss) < abs(lst_star.index(lsl)-lss):
            print("Cool: %s"%lsl)
main(input())
