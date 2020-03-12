#Date: August 15, 2018
#Name: Naon Lee

import random

#Solution 1
def subtractNumbers():
    difference = 0
    num1 = int(input('Input the first whole number: '))
    num2 = int(input('Input the second whole number: '))

    if num1 >= num2:                    #Always subtracting the bigger number from the smaller number
        difference = num1 - num2
    else:
        difference = num2 - num1

    print('The first number was ',num1, 'and the second number was ', num2)         #showing two numbers
    print('The difference between two numbers is ', difference)                     #showing the difference


#Solution 2
def numberList():
    numbersList = []
    
    while len(numbersList) < 10:                        #The process stops when the list contains 10 unique integers
        randomNumber = random.randrange(-20, 20)        #randomly generate number
        
        if randomNumber not in numbersList:             #if the number doesn't exist in the list
            numbersList.append(randomNumber)            #add the number into the list
            
    return numbersList

#Solution 3
def joinWords(wordsDictionary):
    words = ''                                          #String
    
    for v in wordsDictionary.values() :                 
        words = words + v + ' '                         #join the words(values)
        
        print(v)                                        #print the values one per line
        
    return words                                        #return all the words joined as a sentence


#Main program

print('---------------------Solution 1---------------------\n')
#difference of two whole numbers
subtractNumbers()

print('\n---------------------Solution 2---------------------\n')
#create a list of 10 unique random numbers
numbers = numberList()
print('Number List: ', numbers)

print('\n---------------------Solution 3---------------------\n')
#create a sentence
sentence = joinWords({1: 'Python', 2: 'is', 3: 'fun', 4: 'to', 5: 'learn'})
print('\nSentence: ', sentence)

sentence = joinWords({})
print('Sentence: ', sentence)                           #It would return the empty string

