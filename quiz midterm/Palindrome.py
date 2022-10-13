""" Palindrome """

def main():
    """ Palindrome """
    time, start = int(input()), input()
    count, counter = 0, 0
    hour, misn = "", ""
    for i in start:
        if i.isnumeric():
            if count == 0:
                hour += i
            elif count == 1:
                misn += i
        else:
            count += 1
    misn = str(int(misn) + 1)
    while counter != time:
        if len(misn) == 1:
            misn = "0" + misn
        word = hour+misn
        if word == word[::-1]:
            print("%s:%s" %(hour, misn))
            counter += 1
            misn = str(int(misn) + 1)
        else:
            misn = str(int(misn) + 1)
        if misn == "60":
            hour = str(int(hour) + 1)
            misn = "00"
        if hour == "24":
            hour = "0"
            misn = "00"
main()
