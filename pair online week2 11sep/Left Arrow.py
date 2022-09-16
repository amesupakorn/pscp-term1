""" Left Arrow """

def main():
    """ Left Arrow """
    wide = int(input())
    hight = int(input())
    var_k = hight//2
    for i in range(hight):
        if var_k-i >= 0:
            for _ in range(var_k-i):
                print(" ", end="")
        else:
            for _ in range(i-var_k):
                print(" ", end="")
        print("*"*wide)
main()
