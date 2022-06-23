import random
global playerscore
global computerscore
print("WELCOME TO ABRARS CARD GAME")
print("Rules: EACH PLAYER HAS A CARD RANDOMLY ASSIGNED TO THEM GOING AGAINST THE COMPUTER, BASED ON CHANCE -- THE PLAYER CAN EITHER WIN OR LOSE AGAINST THE COMPUTER")
print("****************************************************")
ranger = int(input("How many times would you like to play? (please enter a number) --> "))
print("\n")
for i in range(ranger):
  gameprompt = input("Do you want to play? (Enter Yes or No): ")
  if gameprompt == "Yes":

    print("\n")
    # global variables
    a = random.randint(2,14)
    b = random.randint(2,14)
    c = random.randint(2,14)
    d = random.randint(2,14)
    
    # part 1
    def card2str(ccf):
      
      if ccf == 11:
        ccf = "Jack"
      if ccf == 12:
        ccf = "Queen"
      if ccf == 13:
        ccf = "King"
      if ccf == 14:
        ccf = "Ace"
    
    
      return ccf
    
    # part 2
    def drawcards1():
      if a >= b:
        return f'[{card2str(a)}] [{card2str(b)}]'
      else:
        return f'[{card2str(b)}] [{card2str(a)}]'
    
    def drawcards2():
      if c >= d:
        return f'[{card2str(c)}] [{card2str(d)}]'
      else:
        return f'[{card2str(d)}] [{card2str(c)}]'
    
    
    
    
    # part 3
    def printhand(playercard,txt):
      return playercard + " " + txt
    
    
    print(printhand(drawcards1(),"Your cards"))
    print(printhand(drawcards2(),"Opponent's cards"))
    
    
    def printOutcome(card1, card2, card3, card4):
      # new conditions use if and then elif for related conditions
      if card1 == card2:
        return "You win because your card is tied"
      elif card3 == card4:
        return "Opp win because their card is tied"

      if card1 > (card2 and card3 and card4):
        return "You win because your card is higher"
      elif card2 > (card1 and card3 and card4):
        return "You win because your card is higher"
      elif card3 > (card1 and card2 and card4):
        return "Opponent wins because their card is higher"
      elif card4 > (card1 and card2 and card3):
        return "Opponent wins because their card is higher"


      if card1 == card2 and card3 == card4 and card1 > (card3 and card4):
        return "You win because your card is the highest pair"
      elif card3 == card4 and card1 == card2 and card3 > (card1 and card2):
        return "Opponent wins because their card is the highest pair"

      if card1 > (card2 and card4) and card1 == card3 and card2 > card4:
         return "You win because your card is 2nd highest pair"
      elif card2 > (card1 and card3) and card2 == card4 and card1 > card3:
         return "You win because your card is 2nd highest pair"
      elif card1 > (card2 and card3) and card1 == card4 and card2 > card3:
         return "You win because your card is 2nd highest pair"
      elif card2 > (card1 and card4) and card2 == card3 and card1 > card4:
         return "You win because your card is 2nd highest pair"
      elif card3 > (card2 and card4) and card3 == card1 and card4 > card2:
         return "Opponent wins because their card is 2nd highest pair"
      elif card3 > (card4 and card1) and card3 == card2 and card4 > card1:
         return "Opponent wins because your card is 2nd highest pair"
      elif card4 > (card2 and card3) and card4 == card1 and card3 > card1:
         return "Opponent wins because your card is 2nd highest pair"
      elif card4 > (card1 and card3) and card4 == card2 and card3 > card2:
         return "Opponent wins because your card is 2nd highest pair"


    print("\n")
    print(printOutcome(a,b,c,d))
    print("\n")

  if gameprompt == "No":
    break
