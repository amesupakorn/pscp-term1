"""Kabata"""
def main():
    """Kabata"""
    for _ in range(int(input())):
        txt = input()
        txt = txt.replace('baka', '-').replace("bakka", "").\
            replace("ta", "").replace("ba", "").replace("ka", "")
        if txt == "":
            print("yes")
        else:
            print("no")
main()
