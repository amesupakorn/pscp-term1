"""Impostor"""
def main():
    """Impostor"""
    role, dead, dead_list = [], [], []
    live_list, count = [], 0
    while True:
        txt = input()
        if txt == "Start":
            break
        txt = txt.replace("{", " ").replace("}", " ").replace("\"", " ").replace(":", " ")
        role.append(txt.split())
    role.sort(key=lambda i: i[0])
    while True:
        player = input()
        if player == "End":
            break
        dead.append(player)
    dead.sort(key=lambda i: i[0])
    for i in role:
        if i[0] in dead:
            dead_list.append(i)
        else:
            live_list.append(i)
    for j in live_list:
        if j[1] == "Impostor":
            count += 1
    print("%d Impostor Remains" %count)
    print("***Alive***")
    for k in live_list:
        print("%s : %s" %(k[0], k[1]))
    print("***Dead***")
    for i in dead_list:
        print("%s : %s" %(i[0], i[1]))
main()
