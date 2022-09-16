""" Future Message """

def main():
    """ Future Message """
    text = input()
    if text.isnumeric():
        print("Number")
    elif text.isupper():
        print("Uppercase")
    elif text.islower():
        print("Lowercase")
    elif text.isspace():
        print("Space")
    elif text.istitle():
        print("Title")
    else:
        print("Other")
main()
