import art,random
print(art.logo)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deal_player = random.choice(cards)
    return deal_player

player_cards = []
computer_cards = []


for _ in range(2): # '_' cuz we dont need the variable, just need to run this loop twice.
    player_cards.append(deal_card())
    computer_cards.append(deal_card())



print(player_cards)