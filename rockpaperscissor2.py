import random
print("welcome") 
chars = "RPS"
def rps(player1,player2):
    if player1 == "R" and player2 == "P":
        return "computer won!!"
    elif player1 == "P" and player2 == "R":
        return "player1 won!!"
    elif player1 == "P" and player2 == "S":
        return "computer won!!"
    elif player1 == "S" and player2 == "P":
        return "player1 won!!"
    elif player1 == "R" and player2 == "S":
        return "player1 won!!"
    elif player1 == "S" and player2 == "P":
        return "computer won!!"
    elif player1 not in chars:
        return "wrong input"
    elif player1 == player2:
        return "tie"
run = True
while run:
    player1 = input("R for rock ,P for Paper,S for scissors : \n")
    player2 = random.choice(chars)
    print(rps(player1,player2))
