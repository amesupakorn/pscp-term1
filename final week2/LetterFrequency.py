"""LetterFrequency"""
import string
def main():
    """LetterFrequency"""
    txt = input().lower().replace(" ", "")
    ans = list(filter(lambda a: a in string.ascii_letters, txt))
    ans = max(set(txt), key=txt.count)
    print(ans)
main()
