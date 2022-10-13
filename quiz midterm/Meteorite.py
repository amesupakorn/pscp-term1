""" Meteorite """
def main():
    """ Meteorite """
    numa = float(input())
    numb = int(input())
    numc = float(input())
    time = 0
    count = 0
    while numa >= numc:
        numa = numa / numb
        count += (numb ** time)
        time += 1
    print(count)
main()
