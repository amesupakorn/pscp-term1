"""Filter"""
import json
def main():
    """Filter"""
    dictt = json.loads(input())
    group = ['0']
    score = float(input())
    for i in dictt:
        if dictt[i] >= score:
            group.append('%s %.2f' %(i, float(dictt[i])))
        else:
            pass
    if len(group) >= 2:
        group.remove('0')
    group.sort()
    for i in group:
        if i == "0":
            print("Nope")
            break
        else:
            print("%s\t%.2f" %(i[0:8], float(i[9::])))
main()
