import random

print("Welcome.")
print('You are playing "Rock, paper or scissors" against the computer.')

playing = True

while playing:

    notDraw = True

    while notDraw:

        falseInput = True

        computer = random.choice(["Rock", "Paper", "Scissors"])

        while falseInput:

            player = input("Please choose rock (r), paper (p) or scissors (s): ").lower().capitalize()
            
            if player in ["R", "P", "S"]:
                if player == "R":
                    player = "Rock"
                    falseInput = False
                elif player == "P":
                    player = "Paper"
                    falseInput = False
                elif player == "S":
                    player = "Scissors"
                    falseInput = False

            elif player in ["Rock", "Paper", "Scissors"]:
                falseInput = False

            else: 
                print("This is not a valid choice. Choose again.")
                falseInput= True   

        print(f"You choose: {player}.")
        print(f"Computer choose: {computer}.")

        if player == computer:
            print("Draw.")    
            print("One more time.")  
            print("\n") 
            notDraw = True

        elif player == "Rock":
            if computer == "Paper":
                print("Computer won.")
                notDraw = False
            else: 
                print("You won. Gratulations.")
                notDraw = False
        elif player == "Paper":
            if computer == "Scissors":
                print("Computer won.")
                notDraw = False
            else: 
                print("You won. Gratulations.")
                notDraw = False
        elif player == "Scissors":
            if computer == "Rock":
                print("Computer won.")
                notDraw = False
            else: 
                print("You won. Gratulations.") 
                notDraw = False
     
    morePlaying = True  

    while morePlaying:
        
        playAgain = input("Do you want to play again? (y/n) ").lower().capitalize()

        if playAgain in ["N", "NO"]:
            print("Thanks for playing this game.")
            morePlaying = False
            playing = False

        elif playAgain in ["Y", "Yes"]:
            print("\n")
            morePlaying = False
            Playing = True
        
        else:
            morePlaying = True 
            



    
            
    
