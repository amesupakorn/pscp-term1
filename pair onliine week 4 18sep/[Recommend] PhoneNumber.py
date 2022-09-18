""" [Recommend] PhoneNumber """

def main():
    """ [Recommend] PhoneNumber """
    phone, people = input(), input()
    if len(phone) == 9:
        if people == "Domestic":
            print(phone[0]+" "+phone[1:5]+" "+phone[5:])
        else:
            print("+66"+" "+phone[1:5]+" "+phone[5:])
    else:
        if people == "Domestic":
            print(phone[0:2:]+" "+phone[2:6]+" "+phone[6:])
        else:
            print("+66"+phone[1]+" "+phone[2:6]+" "+phone[6:])
main()
