# Day 14 - Final challenge.


from art import logo, vs
from game_data import data
# from replit import clear
import random

still_playing = True
user_score = 0
while still_playing:
  print(logo)

  print(f"Your current score: {user_score}")

  option_a = data[random.choice(range(0, len(data)))]
  a_ig_followers = option_a['follower_count']
  print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")

  print(vs)

  option_b = data[random.choice(range(0, len(data)))]
  b_ig_followers = option_b['follower_count']
  print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

  option_b = option_a
  option_b = data[random.choice(range(0, len(data)))]

  user_election = input("Who has more followers: 'A' or 'B' ").lower()
  if user_election == 'a':
    if a_ig_followers > b_ig_followers:
      user_score += 1
      print(f"You score {user_score} ")
    #   clear()
    elif a_ig_followers == b_ig_followers:
      print(f"You score {user_score} ")
    else:
    #   clear()
      print(logo)
      print(f"Sorry that's wrong. Final score {user_score} ")
      still_playing = False

  elif user_election == 'b':
    if b_ig_followers > a_ig_followers:
      user_score += 1
      print(f"You score {user_score} ")
    #   clear()
    elif b_ig_followers == a_ig_followers:
      print(f"You score {user_score} ")
    else:
    #   clear()
      print(logo)
      print(f"Sorry that's wrong. Final score {user_score} ")
      still_playing = False
