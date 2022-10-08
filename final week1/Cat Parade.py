"""Cat Parade"""
def main():
    """Cat Parade"""
    position = []
    group = []
    while True:
        txt = input().split(", ")
        #pop ออกเมื่อเจอ dog
        if txt == ["IT\'S A DOG"]:
            position.pop()
            continue
        if txt == ['END']:
            break
        position += (txt)
    #loop กรองสายพันธุ์ว่ามีเท่าไร
    for i in range(len(position)):
        if position[i] not in group:
            group.append(position[i])
    #เรียงa-z
    group.sort()
    #loop ตอบ
    for i in range(len(group)):
        print("%s %d %d"%(group[i], (position.index(group[i])+1), position.count(group[i])))
main()
