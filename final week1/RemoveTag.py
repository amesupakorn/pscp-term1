""" RemoveTag """
def main():
    """ RemoveTag """
    num = input()+" "
    remove = False
    group = []
    txt = ""
    for i in num:
        if i == "<":
            remove = True
        if not remove:
            txt += i
            if i == " " and len(txt.strip()) > 0:
                group.append(txt.strip())
                txt = ""
            elif len(txt.strip()) == 0:
                txt = ""
        elif remove and len(txt.strip()) > 0:
            group.append(txt.strip())
            txt = ""
        if i == ">":
            remove = False
    print(group)
main()
