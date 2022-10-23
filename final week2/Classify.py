""" Classify """
def main():
    """ Classify """
    group = []
    while True:
        num = input()
        if num == "END":
            break
        group.append(num[:4])
    old_year = 0
    for i in sorted(set(group)):
        year = i[:2]
        if year != old_year:
            print(year, int(i[2:4]), group.count(i))
        else:
            print("--", int(i[2:4]), group.count(i))
        old_year = year
main()
