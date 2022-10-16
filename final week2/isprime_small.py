""" isprime_small """
def main(num):
    """ isprime_small """
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
main(int(input()))
