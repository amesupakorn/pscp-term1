""" BigFrame """

def main():
    """ BigFrame """
    txt_1, txt_2, txt_3 = input().rstrip(), input().rstrip(), input().rstrip()
    txt_4, txt_5 = input().rstrip(), input().rstrip()
    findmax = max(len(txt_1), len(txt_2), len(txt_3), len(txt_4), len(txt_5))
    print("**"+("*"*findmax)+"**")
    print('* '+txt_1+(' '*(findmax-len(txt_1)))+' *')
    print('* '+txt_2+(' '*(findmax-len(txt_2)))+' *')
    print('* '+txt_3+(' '*(findmax-len(txt_3)))+' *')
    print('* '+txt_4+(' '*(findmax-len(txt_4)))+' *')
    print('* '+txt_5+(' '*(findmax-len(txt_5)))+' *')
    print("**"+("*"*findmax)+"**")
main()
