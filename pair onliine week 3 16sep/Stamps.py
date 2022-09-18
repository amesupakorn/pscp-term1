""" Stamps """

def main():
    """ Stamps """
    n_input, a_input, b_input = int(input()), int(input()), int(input())
    c_input, d_input = int(input()), int(input())
    stamp, count = 0, 0
    for _ in range(n_input):
        amount = int(input())
        a_discount = amount
        while stamp >= c_input and a_discount > 0:
            stamp -= c_input
            a_discount -= d_input
            if a_discount < 0:
                a_discount = 0
        stamp += int((a_discount / a_input)) * b_input
        count += 0 if a_discount <= 0 else a_discount
    print(int(count))
    print(int(stamp))
main()
