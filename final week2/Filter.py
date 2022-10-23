"""Filter"""
import json
def main():
    """Filter"""
    my_dict = input()
    my_list = ['0']
    test = float(input())
    my_dict = json.loads(my_dict)
    for key in my_dict:
        if my_dict[key] >= test:
            my_list.append('%s %.2f' %(key, float(my_dict[key])))
        else:
            pass
    if len(my_list) >= 2:
        my_list.remove('0')
    my_list.sort()
    for i in my_list:
        if i == "0":
            print("Nope")
            break
        else:
            print("%s\t%.2f" %(i[0:8], float(i[9::])))
main()
