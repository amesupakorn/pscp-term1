""" HorizontalHistogram """
def main():
    """ HorizontalHistogram """
    txt = list(input())
    ans = sorted(set(txt), key=lambda x: (not x.islower(), x))
    for i in ans:
        print(i, end=" : ")
        num = txt.count(i)
        print("".join(["-" if i % 5 else "-|" for i in range(1, num+1)]).rstrip("|"))
main()
