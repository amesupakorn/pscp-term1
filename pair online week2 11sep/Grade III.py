""" Grade III """

def main():
    """ print """
    sec = int(input())
    total = 0
    for _ in range(sec):
        num = gra(float(input()))
        total += num
    ans = ((int((total/sec)*100))/100)
    print("%.2f" %ans)

def gra(num):
    """ return """
    grade = 0
    if num >= 95:
        grade = 4
    elif num >= 90:
        grade = 3.5
    elif num >= 85:
        grade = 3
    elif num >= 80:
        grade = 2.5
    elif num >= 75:
        grade = 2
    elif num >= 70:
        grade = 1.5
    elif num >= 65:
        grade = 1
    elif num >= 60:
        grade = 0.5
    elif num >= 0:
        grade = 0
    return grade
main()
