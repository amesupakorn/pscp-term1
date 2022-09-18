""" [Recommend] BTSMRT """

def main():
    """ [Recommend] BTSMRT """
    day, age, hight = input(), float(input()), float(input())
    if day == "Normal Day" and age < 14 and hight < 90:
        print("FREE")
    elif day == "Children Day" and age < 14 and hight <= 140 or age < 14 and hight < 90:
        print("FREE")
    elif day == "Senior Day" and age >= 60 or age < 14 and hight < 90:
        print("FREE")
    else:
        print("PAY")
main()
