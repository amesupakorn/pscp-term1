""" diamond """

def main(num):
    """ diamond """
    asterisk = num//2
    for i in range(num):
        for j in range(num):
            if i == asterisk or i+j == asterisk or j-i == asterisk \
            or i-j == asterisk or j == num-i+asterisk-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
