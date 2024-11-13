from art import logo
import random

# generate random card from deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# sums cards total
def calculate_scores(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# compare and decide winner or loser
def compare(u_score, c_score):
    if c_score == u_score:
        return "Draw"
    elif c_score == 21:
        return "Lose, opponent has Blackjack"
    elif u_score == 21:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

# main game function
def play_game():
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    while not is_game_over:
        for i in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        computer_score = calculate_scores(computer_cards)
        user_score = calculate_scores(user_cards)

        print(f"Your cards: {user_cards}, current_score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            deal_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if deal_another == "y":
                user_cards.append(deal_card())
            elif deal_another == "n":
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    print("======Results======")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# start game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    play_game()
