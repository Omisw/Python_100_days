# Day 9 - Final challenge.


from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

auction = True
bidders = {}

def winner_bid(best_bid):
  winner_bid = 0
  winner = ""
  for bidder in best_bid:
    heighest_bid = best_bid[bidder]
    if winner_bid < heighest_bid:
      winner_bid = heighest_bid
      winner = bidder
  print(f"The winner is {winner}, with the heighest bid of ${winner_bid} ")

while auction == True:
  name_sale = input("Want to joint to the auction, what's your name? ").lower()
  bid = int(input("How much do you want to bid? $"))
  more_people = input("Theres someone else that want to bid? Type 'Yes' or 'No' ").lower()

  bidders[name_sale] = bid

  if more_people == "yes":
    auction = True
    
  elif more_people == "no": 
    auction = False
    
    winner_bid(bidders)
    
    