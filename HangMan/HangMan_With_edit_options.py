# This programs deals with handling of both Hangman_text.txt and words.json handling 
# we can edit and update the text file and json file if the given arguments are still valid

import json
import random

def read_content(file_name,mode='r')->dict:
    f = open(file_name,mode)
    if mode == 'r':
        dictnory = {}
        for i,j in zip(iter(f),iter(f)):
            dictnory[i.strip('\n')] = j.strip('\n')
        return dictnory
    print("Not possible to load")
    exit(1)
#read the string the entered choices till now
#it prints the word with letters that are entered and others with '_'
def display_word_with_letters(word,letters):
    # it prints the letters that are choisen by the user 
    for i in word :
        print("_ ",end="") if i not in letters else print(i,end=" ")

def edit_text_file(mode):
    if mode.lower() in ['w','a','a+','w+','r','r+']:
        with open(r'C:\Users\VIVEK VR\Documents\Python\HangMan\hangman_text.txt',mode.lower()) as file:
            if mode.lower() in ['w','w+']:
                print('Are you sure you wanna erase the data in the file?')
                Choice = input("if you wanna rewrite the file press 'YES'or'Y' else 'NO'or'N'")
                if Choice.upper() in ['YES','Y']:
                    edit = 1
                    while edit:
                        x = input("Give the name of the word to add")
                        file.write(x)
                        x = input("Enter the description regerding the word")
                        file.write(x)
                        x = input('Wanna continue to add more')
                        edit = 1 if x.upper() in ['YES','Y'] else 0
                    return 0
                else:
                    print("If you wanna add new words to the file the use the mode as append or 'a' or 'a+'")
            elif mode.lower() in ['a','a+']:
                edit = 1
                while edit:
                    x = input("Give the name of the word to add")
                    file.write(x)
                    x = input("Enter the description regerding the word")
                    file.write(x)
                    x = input('Wanna continue to add more')
                    edit = 1 if x.upper() in ['YES','Y'] else 0
                return 0
            elif mode.lower() in ['r','r+']:
                return read_content(r'C:\Users\VIVEK VR\Documents\Python\HangMan\hangman_text.txt')
    else:
        print("Try entering a valid choice like in [a,a+,w,w+,r,r+]")

def update_json():
    with open(r'C:\Users\VIVEK VR\Documents\Python\HangMan\words.json','w') as file:
        file.write(json.dumps(read_content(r'C:\Users\VIVEK VR\Documents\Python\HangMan\hangman_text.txt')))


def dev_module():
    user_name = input('Username:').strip()
    pass_code = input('Passcode:').strip()
    dev = 0
    if user_name == 'EDIT' and pass_code == '0000':
        dev = 1
    else:
        print('well try getting the correct credential')
    while dev:
            x = input('Enter the responce').strip()
            if x.lower() == 'help':
                print('To open the file in write use w')
                print('To open the file in append use a')
                print('exit to get out')
            elif x.lower() in ['w','w+','a','a+']:
                dic = edit_text_file(x)
                dev = 0
                update_json()
            elif x.lower() == 'exit':
                dev = 0
            else:
                print('Try valid responses or enter exit, to get out or help, to get help')

############################################################################################################################
############################################################################################################################
############################################################################################################################

print('*'*98)
print('HANGMAN'.center(98,'*'))
print('*'*98)
print()
print('Are you new to the game?')
print('Here are some rules for you')
with open(r"C:\Users\VIVEK VR\Documents\Python\HangMan\rules.txt",'r') as f:
    for line in f.readlines():
        print('**',line.strip('\n'))
print()
print('If you wanna edit the files regarding the game, Enter edit')
print('If you wanna play the game, Enter play')
y = input('EDIT/PLAY')

if y.strip().lower() == 'edit':
    dev_module()
elif y.strip().lower() == 'play':
    dic = edit_text_file('r')

    print("Ready to Start? (Yes/No // Y/N // yes/no // y/n)")

    enter = input()

    while enter.strip().upper() in ['YES','Y']:

        string = random.choice(list(dic.keys()))# a randdom word from the list
    
        print("***",dic[string],"***")#hint related to the random string
        print("It is a",len(string),"lettered word")
    
        print("\nGuess: ","_ "*len(string),sep="") # Guess template
        chances = random.randint(len(set(string)),len(set(string))+2) # chances given to user to find the word
    
        print("\nYou have",chances,"chances to guess the word either the choices are correct or wrong")
        print()
    
        i = 1
        correct_choices = 0 #list the number of unique correct choices 
        letter_choices = [] # stores teh letters that are selected by the user
    
        while i<=chances and correct_choices < len(set(string)): # continue if user complete the word or chances are completed
    
            print("\nYour choice of letter is:",end=" ")
            choice = input().strip() # entering choice
            i += 1
            if choice.isalpha() and len(choice) == 1:
            
                if choice.upper() in string:
            
                    if choice.upper() not in letter_choices: # if the user's choice is not a repeated one tehn it adds to the choice list
                        print("\nThe letter",choice,"is in the word")
                        letter_choices.append(choice.upper())
                        #Display the word with fxn display_word_with_letters(word,letter)
                        display_word_with_letters(string,letter_choices)
                        correct_choices += 1
                    else:
                        print("It's already used.\nTry another one.")
            
                else: #If the user gave a invalid choice 
                    print("Sorry, your choice is not in the word.\nTry Again")
                    print("Need Hint. Then press 'h' else Press Enter to continue.")
                    if input().strip().lower() == 'h': # for Hints
                        print('Sorry, Hints are not yet provided.')
            else:
                print("Please, enter a Valid choice")


        if correct_choices == len(set(string)):
            print("\nCongrats, you found the word:",end=" ")
            print(string)
        else: print("Sorry try again")


        print("Ready for another round (Yes/No // Y/N // yes/no // y/n)")
        enter = input().strip()


    else:
        print("Wishing you good for next time")
        print("Bye!")
    
x = input("Like to edit the source_file")
if x.strip().lower() in ['yes','y']:
    print('username:EDIT')
    print('passcode:0000')
print('Have a good day')