""" Elo """

def main():
    """ Elo """
    numa, numb, want = int(input()), int(input()), input()
    if want == "A":
        elo = 1/(1+(10**((numb-numa)/400)))
    elif want == "B":
        elo = 1/(1+(10**((numa-numb)/400)))
    print("%.2f" %elo)
main()
