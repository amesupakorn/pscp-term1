""" Duplicate I """
def main():
    """ Duplicate I """
    group1 = set()
    group2 = set()
    num_m, num_n = int(input()), int(input())
    for _ in range(num_m):
        data_m = input()
        group1.add(data_m)
    for _ in range(num_n):
        data_n = input()
        group2.add(data_n)
    ans = group1.intersection(group2)
    ans_real = (sorted((ans), reverse=True))
    if ans == set():
        print("Nope")
    else:
        for i in ans_real:
            print(i)
main()
