""" Sequence XII """

def main(num):
    """ Sequence XII """
    for i in range(-num+1, num):
        for j in range(-num+1, num):
            print("%02d"%(num-abs(abs(i)-abs(j))), end=" ")
        print()
main(int(input()))
