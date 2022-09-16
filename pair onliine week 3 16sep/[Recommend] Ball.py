""" [Recommend] Ball """

def main(hight):
    """ [Recommend] Ball """
    count = -1
    while hight >= 0.01:
        hight *= (3/5)
        count += 1
    print(count)
main(float(input()))
