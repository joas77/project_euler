# https://projecteuler.net/problem=54

class Card:
    cards_rank = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
    SUITS = {
        "C": "Clubs",
        "D": "Diamonds",
        "H": "Hearts",
        "S": "Spades",
        "J": "Jack",
        "Q": "Queen",
        "K": "King"
    }

    def __init__(self, card):
        self.card = card
        self.value = self.cards_rank[card[0]]
        self.suite = card[1]

    def __str__(self):
        return super().__str__()

class Poker:
    def __init__(self, cards):
        self.cards = [Card(c) for c in cards]

    def high_card(self):
        highest_card = self.cards[0]

        for card in self.cards:
            if card.value > highest_card.value:
                highest_card = card

        return highest_card


    def flush(self):
        has_flush = False
        suite = self.cards[0]
        for card in self.cards:
            pass

if __name__ == "__main__":
    
    player1 = Poker(["5H", "5C", "6S", "7S", "KD"])
    print(player1.high_card())