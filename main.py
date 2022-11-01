from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
bid_continue = True

def max_bid_amount(final):
  for i in final :
    max = 0
    bidder = final[i]
    name_of_bidder = ''
    if bidder> max :
      max = bidder
      name_of_bidder = i
  print(f"{name_of_bidder} has highest bid with amount {max}")
      
while bid_continue:
  name = input("Enter your name? ")
  bid_amount = int(input("Enter your bidding amount:$"))
  in_dict = {name : bid_amount}
  more_bid = input("Did u want to continue bidding ?yes/no ").lower()
  if(more_bid == "no"):
    bid_continue = False
    max_bid_amount(in_dict)
  elif(more_bid == "yes"):
    clear()
    
