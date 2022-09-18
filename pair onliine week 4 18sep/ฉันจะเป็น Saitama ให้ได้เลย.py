""" ฉันจะเป็น Saitama ให้ได้เลย """
import math
def main():
    """ ฉันจะเป็น Saitama ให้ได้เลย """
    pushup, situp, updown = int(input()), int(input()), int(input())
    run, day_pushup, day_situp = int(input()), int(input()), int(input())
    day_run, day_updown = int(input()), int(input())
    how_pushup, how_situp = math.ceil(pushup/day_pushup), math.ceil(situp/day_situp)
    how_updown, how_run = math.ceil(updown/day_updown), math.ceil(run/day_run)
    total = 0
    if total < how_pushup:
        total = how_pushup
    if total < how_situp:
        total = how_situp
    if total < how_updown:
        total = how_updown
    if total < how_run:
        total = how_run
    print(total)
main()
