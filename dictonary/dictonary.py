import json
#import time
import re
from collections import Counter

#initial_time = time.time()


with open(r'C:\Users\VIVEK VR\Documents\Python\dictonary\abc.json','r') as file:
    data = json.load(file)


#print(data)

#with open(r'C:\Users\VIVEK VR\Documents\Python\dictonary\big.txt','w+',encoding="utf-8") as file:
#    for i in data.keys():
#        file.write(i+'\n')

#SpellChecker
###The below piece of code is an extract from norvig.com\spell-correct.html

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open(r'C:\Users\VIVEK VR\Documents\Python\dictonary\big.txt',encoding="utf-8").read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
###The above piece of code is an extract from norvig.com\spell-correct.html



word = input('Enter the word to get the meaning\n')
word = word.lower()
if word != correction(word):
    print("Do you mean: ",correction(word))

if correction(word) in data.keys():
    sno = 1
    for i in data[correction(word)]:
        print(sno,i,sep=" ")
        sno +=1 
else:
     print('Not valid results are found')


#final_time = time.time()
#print("TimeTaken: ", final_time-initial_time)