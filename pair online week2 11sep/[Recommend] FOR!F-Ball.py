""" FOR!F-Ball """

def main(txt):
    """ FOR!F-Ball """
    position = ["ball", "fake1", "fake2"]
    for i in range(len(txt)):
        pos = txt[i:i+1]
        if pos == "A":
            temp = position[0]
            position[0] = position[1]
            position[1] = temp
        elif pos == "B":
            temp = position[1]
            position[1] = position[2]
            position[2] = temp
        elif pos == "C":
            temp = position[2]
            position[2] = position[0]
            position[0] = temp
    print((position.index("ball"))+1)
main(input())
