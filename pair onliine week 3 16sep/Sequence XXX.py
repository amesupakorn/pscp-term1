""" Sequence xxx """

def main():
    """ Sequence xxx """
    num1, num2 = int(input()), int(input())
    ans = num1 // 2
    for i in range(-ans, ans+1):
        for _ in range(num2):
            for j in range(-ans, ans+1):
                if abs(i) == abs(j) or j == -ans or j == ans or i == -ans or i == ans:
                    txt = "%s" %("*")
                    print(txt, end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        print()
main()
