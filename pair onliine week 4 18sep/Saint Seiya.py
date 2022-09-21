""" Saint Seiya """

def main(punch_se, punch_key):
    """ Saint Seiya """
    punch_2, punch_6 = (punch_se//2 - punch_se//6), punch_se//6
    punch = (punch_2 * 165) + punch_6
    if punch < punch_key:
        return punch
    punch = (punch_key//331)*331 #ต่อย 6 วิ
    temp_time = (punch//331)*6
    if punch >= punch_key:
        temp_time += 1
    elif punch + 165 >= punch_key:
        punch += 165
        temp_time += 3
    elif punch + 330 >= punch_key:
        punch += 330
        temp_time += 5
    else:
        punch += 331
        temp_time += 6
    if punch_se - temp_time > 0:
        punch += (punch_se - temp_time)*12
    return punch
print(main(int(input()), int(input())))
