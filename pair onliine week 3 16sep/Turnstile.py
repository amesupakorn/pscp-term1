""" Turnstile """

def main():
    """ Turnstile """
    all_action = []
    first = ""
    people = 0
    while True:
        action = input()
        if action == "END":
            break
        else:
            all_action.append(action)
    for i in all_action:
        if i == "C":
            first = "C"
        if first + i == "CP":
            people += 1
            first = ""
    print(people)
main()
