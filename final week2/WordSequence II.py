"""WordSequence II"""
def main(txt1, txt2):
    """WordSequenceII"""
    for i in range(0, max(len(txt1), len(txt2))+1):
        print(txt2[:i]+txt1[i:])
main(input(), input())
