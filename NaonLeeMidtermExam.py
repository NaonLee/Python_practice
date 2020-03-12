#Name : Naon Lee
#Date : June 20, 2018
#Purpose: Miterm exam


def listProgram() :

    num = float(input('Please type the number (the number should be negative real/float number) :'))
    if num >= 0 :
        print('\n!Wrong number has been typed, input is end!\n')
    return num

conf = 'continue'
conf = conf.lower()
while conf != 'quit' : 
    print('(If you want to end typing the numbers, please type any number >= 0)\n')
    numList = []
    value = listProgram()

    while value < 0 :    
        numList.append(value)
        print(value, 'is input in the list')
        value = listProgram()

    if len(numList) == 0 :
        print('\n!There is no number in the list!\n')
    
    else :
        
        print('--------------------------Numbers in the list---------------------------')
        for i in numList :
            print(i)
        print('------------------------------------------------------------------------')

        
        index = -1
        search = float(input('Please input the number what you want to find (must be less than 0):'))
        for i in numList :
            if i == search :
                index = numList.index(i)
        if index == -1 :
            print('\n!There is no', search,'in the list!\n')
        else :
            print('\nThe number what you want :', numList[index], 'and its first occurrence in the list is ', numList[0],'\n')



        
        
        print('\n----------------Numbers in the list(the position start 1)----------------')
        for i in range(1,len(numList)) :
            print(numList[i])
        print('-------------------------------------------------------------------------')
        
        numList.remove(numList[-1])
        print('\n------------Numbers in the list(after deleting ths last number)-----------')
        if len(numList) == 0 :
            print('The list is empty')
        print(numList[:])
        print('------------------------------------------------------------------------')

        numList.sort()
        print('\n--------------------Numbers in the sorted list---------------------')
        print('The list is empty')
        print(numList[:])
        print('------------------------------------------------------------------------')

    

    conf = input('\n\nIf you want to quit this program, plese type \'Quit\' :')
    conf = conf.lower()

