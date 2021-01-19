import random
# from replit import clear
from art import logo

play_blackjack = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
if play_blackjack == "yes":
#   clear()
  print(logo)
elif play_blackjack == "no":
  print("No more play")

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card

my_hand = []
computer_hand = []
my_hand.append(deal_card())
my_hand.append(deal_card())
computer_hand.append(deal_card())

print(f"Your cards {my_hand}, your current {sum(my_hand)}")
print(f"Your cards {computer_hand}")

def total_cards(list):
  sum_cards = sum(list)
  return sum_cards
  
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and cards > 21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)

game_over = True
while game_over:
  take_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  
  if take_card == "y":
    my_hand.append(deal_card())
    print(f"Your cards {my_hand}, your current score: {total_cards(my_hand)}")
    print(f"Computer hand {computer_hand}, your current score: {total_cards(computer_hand)}")
    calculate_score(my_hand)
    if sum(my_hand) > 21:
      print("You lose")
      game_over = True
  elif take_card == 'n':

    computer_life = True
    while computer_life:
      if total_cards(computer_hand) < 21:
        computer_hand.append(deal_card())
      elif total_cards(computer_hand) >= 21:
        if sum(computer_hand) > 21:
          print("You win")
        computer_life = False
        game_over = True
      print(f"Computer hand {computer_hand}, your current score: {total_cards(computer_hand)}")

    game_over = False
