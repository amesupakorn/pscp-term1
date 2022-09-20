""" [Recommend] Books """
import math
def main():
    """ [Recommend] Books """
    book, page, numx = int(input()), int(input()), int(input())
    numy = int(input())
    day, count, allread = 0, 0, 0
    while True:
        counter = math.ceil((numx / numy) * page)
        if count == book:
            break
        if counter >= page:
            break
        allread += counter
        if allread >= page:
            count += 1
            allread = 0
        numx += 1
        numy += 1
        day += 1
    day += (book - count)
    print(day)
main()
