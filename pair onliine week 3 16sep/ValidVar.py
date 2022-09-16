""" ValidVar """

def main():
    """ ValidVar """
    num = int(input())
    punctuation = ('!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.',\
             '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', ' ', '`',\
             '{', '|', '}', '~')
    word = ('if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break',\
            'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not',\
            'def', 'None')
    for j in range(num):
        validity = True
        total = 0
        variable = input()
        for j in variable:
            total += 1
            if j.isnumeric():
                validity = False
            elif total == 1:
                break
        if variable in word:
            validity = False
        for j in variable:
            if j in punctuation:
                validity = False
        if validity:
            print("Valid")
        else:
            print("Invalid")
main()
