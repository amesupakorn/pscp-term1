""" Sequence XI """
def main(num):
    """ Sequence XI """
    for i in range(-num+1, num, 1):
        for j in range(-num+1, num, 1):
            if abs(i) > abs(j)-1:
                print("%02d"%(num-abs(i)), end=" ")
            else:
                print("%02d"%(num-abs(j)), end=" ")
        print()
main(int(input()))
