"""Impostor"""
import json
def main():
    """Impostor"""
    player, dead, live = {}, {}, {}
    impostor = 0
    while True:
        txt = input()
        if txt == "Start":
            continue
        if txt == "End":
            break
        if txt[0] == "{":
            player.update(json.loads(txt))
        else:
            dead.update({txt:player[txt]})
    for i in player:
        if i not in dead:
            live.update({i:player[i]})
    for i in live:
        if player[i] == "Impostor":
            impostor += 1
    print(str(impostor)+" Impostor Remains", "***live***", sep="\n")
    for i in sorted(live.items(), key=lambda item: item[0]):
        print(*i, sep=" : ")
    print("***Dead***")
    for i in sorted(dead.items(), key=lambda item: item[0]):
        print(*i, sep=" : ")
main()
