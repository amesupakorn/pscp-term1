""" Century """
import math
def main():
    """ Century """
    for _ in range(int(input())):
        year = input()
        if year[:4] == "B.E." and int(year[5:])-543 >= 0:
            year = int(year[5:]) - 543
            print(math.ceil(year/100))
        elif year[:4] == "A.D." and int(year[5:]) >= 0:
            year = int(year[5:])
            print(math.ceil(year/100))
        else:
            print("ERROR")
main()
