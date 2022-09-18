""" [Recommend] Squid Game 3 - Tug-of-War """

def main():
    """ [Recommend] Squid Game 3 - Tug-of-War """
    totala = 0
    totalb = 0
    for _ in range(10):
        totala += int(input())
    for _ in range(10):
        totalb += int(input())
    if totala < totalb:
        print("A")
    elif totalb < totala:
        print("B")
    else:
        print("AB")
main()
