""" Muddled Menu """
def main():
    """ Muddled Menu """
    menu = []
    while True:
        couse = input()
        if couse == "DONE":
            break
        elif couse == "CLOSED":
            return print("Full Course: [] Reversed: []")
        elif couse == "SOMETHING'S WRONG":
            menu.clear()
        elif couse[0:10:] == "Can't do: ":
            menu.remove(couse[10::])
        else:
            couse = couse.split(" #")
            if couse[1].isnumeric():
                menu.insert(int(couse[1])-1, couse[0])
            elif couse[1] == "N":
                menu.append(couse[0])
    print("Full Course: %s Reversed: %s" %(menu, menu[::-1]))
main()
