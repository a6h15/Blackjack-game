import art,random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deal_player = random.choice(cards)
    return deal_player

def calculate_score(cards):
    """Takes the list of cards as input and returns the score."""
    if sum(cards)==21 and len(cards)==2:
        return 0 # comp will know that the cards at hand makes blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(p_score, c_score):
    """Compares the user score player_score against the computer score comp_score."""
    if p_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif p_score == 0:
        return "Win with a Blackjack 😎"
    elif p_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif p_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def game_loop():
    print(art.logo)
    player_cards = []
    computer_cards = []
    comp_score = -1 #for the while loop that plays as the computer.
    player_score = -1
    game_over = False

    for _ in range(2): # '_' cuz we don't need the variable, just need to run this loop twice.
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        comp_score = calculate_score(computer_cards)

        print(f"Your cards : {player_cards} ,current score : {player_score}")
        print(f"Computer first card : {computer_cards[0]}")

        if player_score == 0 or comp_score == 0 or player_score > 21: #0 as when the sum is 21 we return 0 , that's the condition
                game_over = True
        else:
            player_deals = input(f"Type 'y' to take another card or type 'n' to pass")
            if player_deals == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)


    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {comp_score}")
    print(compare(player_score, comp_score))

while input("Do you want to play another game of BlackJack : 'y' or 'n'") == 'y':
    print("\n"*20)
    game_loop()

