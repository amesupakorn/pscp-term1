"""CuteCat CuteFox"""
def main():
    """CuteCat CuteFox"""
    catdict, catsult = {}, {}
    for _ in range(int(input())):
        txt = str(input())
        if len(txt.split('"')) > len(txt.split("'")):
            catdict[txt.split('"')[1]] = txt.split('"')[3]
        else:
            catdict[txt.split("'")[1]] = txt.split("'")[3]
    countcat, countfox = main1(catdict, "Cat"), main1(catdict, "Fox")
    checkcat, checkfox, count = "Cat01" in catdict.values(), "Fox01" in catdict.values(), 0
    if countcat == 0 or checkcat == 0:
        catsult["Garfield"] = "Cat01"
    if countfox == 0 or checkfox == 0:
        catsult["Fubuki"] = "Fox01"
    for key, value in sorted(catdict.items(), key=lambda x: x[1]):
        if checkfox == 0 and value.count("Fox") >= 1 and count == 0:
            count += 1
            catsult["Fubuki"] = "Fox01"
        catsult[key] = value
    countcat, countfox = main1(catsult, "Cat"), main1(catsult, "Fox")
    cat, fox = {}, {}
    for key, value in catsult.items():
        if value.count("Cat") >= 1:
            cat.update({int(value.split("Cat")[1]): [key, value]})
        elif value.count("Fox") >= 1:
            fox.update({int(value.split("Fox")[1]): [key, value]})
    print("Cat : %d\nFox : %d" %(countcat, countfox))
    for cry in sorted(cat):
        print(cat[cry][0] + " : " + cat[cry][1])
    for cry in sorted(fox):
        print(fox[cry][0] + " : " + fox[cry][1])
def main1(catdict, txt):
    """ fuc main """
    return len([i for i in catdict.values() if txt in i])
main()
