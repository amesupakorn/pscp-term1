""" SecondConverter """

def main():
    """ SecondConverter """
    center_k, sec_mw, min_mw, h_mw = int(input()), int(input()), int(input()), int(input())
    ans_min = center_k // sec_mw
    ans_h = ans_min // min_mw % h_mw
    ans_sec = center_k % sec_mw
    ans_min = ans_min % min_mw
    ans_h = ans_h % h_mw
    print("%d:%d:%d" %(ans_h, ans_min, ans_sec))
main()
