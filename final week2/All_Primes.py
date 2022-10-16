""" All_Primes """
def main(num):
    """ All_Primes """
    total = 0
    for i in range(1, num+1):
        if  i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                total += 1
    print(total)
main(int(input()))
 