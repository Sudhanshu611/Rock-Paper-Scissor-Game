import random

print("""***
Winning rules of the game ROCK PAPER SCISSORS are :
Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Paper vs Scissors -> Scissor wins
***
""")

while True:
    start_ans = 0 # for restarting game
    print("""***
Type the numeral to select following:
1. Rock
2. Paper
3. Scissor
***
""")
    
    option_dict = {1:"Rock", 2:"Paper", 3:"Scissors"}
    
    #Chances = 3
    chances = 3
    
    #score
    user_score = 0
    opp_score = 0   
    
    
    #game starts
    while chances != 0:
        
        #Computer's selection
        option = '1 2 3'
        option = option.split(' ')
        opp_selection = random.choice(option)
        opp_selection = int(opp_selection)
    
        #User selection
        user_selection = input("Type Your Option Here: ")

        #Mistakes by user
        if not user_selection.isdigit():
            print("Please select between 1-3 only.")
            continue
        elif len(user_selection) > 1:
            print("Please select between 1-3 only and it should be single digit only")
            continue
        elif int(user_selection) > 3 or int(user_selection) < 1:
            print("Please select between 1-3 only.")
            continue
        elif user_selection == '':
            print("Please select between 1-3 only.")
            continue
        

        user_selection = int(user_selection)
        print("You Chose:", option_dict[user_selection])
        print("Opponent Chose:", option_dict[opp_selection],'\n')
        
        #Draw
        if user_selection == opp_selection:
            print("Tie\n")
            print("User Score:", user_score, "Opponent Score:", opp_score,'\n')
            
        # opponents wins
        # 1-2, 2-3, 3-1
        if (user_selection == 3 and opp_selection == 1) or (user_selection == 1 and opp_selection == 2) or (user_selection == 2 and opp_selection == 3):
            print("Opponent won this round\n")
            chances -= 1
            opp_score += 1
            print("User Score:", user_score, "Opponent Score:", opp_score,'\n')
            
        # user wins
        # 1-3,2-1,3-2
        elif (user_selection == 1 and opp_selection == 3) or (user_selection == 2 and opp_selection == 1) or (user_selection == 3 and opp_selection == 2):
            print("You won this round\n")
            chances -= 1
            user_score += 1
            print("User Score:", user_score, "Opponent Score:", opp_score,'\n')
        
    if user_score > opp_score:
        print("!!!You Won by", user_score - opp_score, "score.!!!\n")
    elif user_score < opp_score:
        print("!!!Opponent Won by", opp_score - user_score, "score.!!!\n")
    
    
    
    while True:
        start_again = input("\nDo you wanna restart game? (Y/N): ")
        start_again = start_again.lower()
        if start_again.isdigit():
            print("Type Y/N only.")
        elif start_again == "y":
            print("Hell Yeah")
            start_ans = 1
            break
        elif start_again == "n":
            exit()
        else:
            print("Type Y/N only.")
    if start_ans == 1:
      continue 