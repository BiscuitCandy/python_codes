import random
# Enter Player Name
player = input("Enter player Name : ")
# Heading
print("*" * 98)
print("Rock,Paper&Scissors".center(98,'-'))
print("*"*98)

print(player, "v/s Doddle4z")

print("You play 5 rounds the one wins more rounds wins")

player_score = 0
computer_score = 0
# 5 rounds
for _ in range(5):
    # Round no
    print("-------------")
    print("Round : ",_+1)
    print("-------------")
    #Scores
    print(player,':',player_score,"points")
    print("Doodle4z :",computer_score,"points")

    # Player's choice
    player_choice = input('Enter your choice : ')
    player_choice = player_choice.lower()

    # invalid input
    if player_choice not in ['rock','paper','scissors']:
        print("Sorry invalid, round tied")
    
    # valid input
    # compares the choices 
    # chooses the winner of each round
    else:
        # win sequence for player
        win_choices = {'rock': 'scissors', 'paper':'rock', 'scissors':'paper'}
        #computer choices
        computer_choice = random.choice(['rock','paper','scissors'])
        print("Doodle4z choose -",computer_choice)
        # if both choice same choice
        if player_choice == computer_choice :
            print('Round tied')
            print('Equal Score added')
            player_score += 1
            computer_score += 1
        # if player follows win sequence 
        elif win_choices[player_choice] == computer_choice:
            print(player,'Wins the round -',_+1)
            player_score += 1
        # if computer follows the win sequence
        else:
            print("Doodle4z Wins the round -",_+1)
            computer_score += 1
# final scorecard
print(player,':',player_score,"points")
print("Doodle4z :",computer_score,"points")
# declaring winner
if player_score > computer_score :
    print(player,"won the game")
    print("Congrats,",player.capitalize())
elif player_score < computer_score:
    print("Doodle4z won the game")
    print("Better Luck next time, kiddo")
else:
    print("Game tied")
print("Good playing with ya \nSee you soon")