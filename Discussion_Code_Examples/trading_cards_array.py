class TradingCard:
    def __init__(self, name, set, price):
        self.name = name
        self.set = set
        self.price = price

card1 = TradingCard("Pikachu", "Base Set", 5)
card2 = TradingCard("Alakazam EX", "Scarlet & Violet", .25)
card3 = TradingCard("Gengar", "Scarlet & Violet", .01)

card_array = [card1, card2, card3]

for card in card_array:
    print (card.name, card.set, card.price)