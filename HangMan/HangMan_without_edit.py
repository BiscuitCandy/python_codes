import random
import json
#define a function to read and add the details and hints to the game
#attempt 1
#the file is filled with a name and a hint following in the next line
#inputs are file we are opening and the mode we are opening it default read mode
#returns the data in the form dictonary
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
        print("_",end="") if i not in letters else print(i,end="")
        
dic = read_content(r"C:\Users\VIVEK VR\Documents\Python\HangMan\hangman_text.txt")


#with open(r'C:\Users\VIVEK VR\Documents\Python\HangMan\words.json','w') as file:
#    file.write(json.dumps(dic))


#heading
print("************************************")
print('***************HANGMAN**************')
print("************************************")

print("Ready to Start? (Yes/No // Y/N // yes/no // y/n)")

enter = input()

while enter.upper() in ['YES','Y']:

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
        choice = input() # entering choice
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
                if input().lower() == 'h': # for Hints
                    print('Sorry, Hints are not yet provided.')
        else:
            print("Please, enter a Valid choice")


    if correct_choices == len(set(string)):
        print("\nCongrats, you found the word:",end=" ")
        print(string)
    else: print("Sorry try again")


    print("Ready for another round (Yes/No // Y/N // yes/no // y/n)")
    enter = input()


else:
    print("Wishing you good for next time")
    print("Bye!")