"""	BreachTheDoor """
def main():
    """ BreachTheDoor """
    for i in ''.join(list(filter(lambda x: bool(x.isalpha() or x == ' '), input()))).split():
        if len(i) > 6:
            print(i, end=' ')
main()
