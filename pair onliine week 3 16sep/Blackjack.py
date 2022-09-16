""" Blackjack """

def main():
    """ blackjack """
    var_cards = []
    ace = 0
    total = 0
    num = int(input())
    if num == 2 or num == 3:
        for _ in range(num):
            var_cards.append(input())
        for card in var_cards:
            card = card.upper()
            if card == "J" or card == "K" or card == "Q":
                total += 10
            elif card == "A":
                total += 11
                ace += 1
            elif card.isnumeric():
                if int(card) >= 2 and int(card) <= 10:
                    total += int(card)
        while total > 21 and ace > 0:
            total -= 10
            ace -= 1
    print(total)
main()
