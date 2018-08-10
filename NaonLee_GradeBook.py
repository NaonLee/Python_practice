#Name: Naon Lee
#Date: July 15, 2018
#purpose: Code a Python program to allow an instructor to store marks in assignments during the semester of the students.

MAX_MARK = 10
MIN_MARK = 0
STOP_MARKING = -1

def rangeDef(mark):                 #Function to define the range of mark entering by the user 
    while True:                     #If user type mark which is out of range, this loop makes the user retype
        try:                        #A specific sentence that error can be occurred
            mark_input = int(input(mark))
        except ValueError:          #If the mark typed by the user cannot be translated to integer(float or string)
            print('The mark must be a whole number in the range of 0 to 10') 
        else:
            if 1 <= mark_input <= MAX_MARK or mark_input == STOP_MARKING:       #If the mark typed is in the range(0~10) or -1
                return mark_input                               #Return the mark that user typed
            else :                                              #If the mark is out of the range
                print('The mark must be a whole number in the range of 0 to 10')


def printGrade(GradeBook):                              #Function to print the marks
    print('\n\n============================Grade List============================\n')     #After the end of the program, print the grade list
    for k, v in GradeBook.items() :                                                         #Get the keys and values from an item in the dictionary
        print('---------------------Student Number: ', k, ' ---------------------\n')
        print('Number of Assignments: ', len(v))                                            #length of the key(the number of marks)
        if len(v) != 0 :                                                                    #If the mark(s) exists
            print('Assignment mark(s): ', v)
            print('Average of mark(s): ', "%0.2f" % float(sum(v)/len(v)), '\n')                   #Average with two places after the decimal
print('=====================================================================\n')

                
stdNum = 'continue'
GradeBook = {}                               #Dictionary to put the student number and marks
stdNum = str(input('Enter student number (enter end to stop the program):'))

while stdNum.lower() != 'end' :             #If the user enter end(in any case combination), end the program
        
    
    if GradeBook.get(stdNum.lower()) or GradeBook.get(stdNum.upper()) :      #To check whether the student number(in any case combination) already exist
        print('The student number ' + str(stdNum) +' already exists.')
    else :
        GradeBook.setdefault(stdNum)        #Put the student number in the dictionary as a key
        markList = []                       #List to put the marks
        mark = 0
        count = 1
        print('\nPlease enter marks of assignments:', stdNum)
        print('(A maximum of five assignments were given to the students)')
        print('(You can enter -1 to stop giving marks)\n')
        
        while count < 6 and mark != STOP_MARKING :            #If the user typed -1 or marks have been entered into five assignments, entering mark program will stop
            
            mark = rangeDef('Assignment '+ str(count) +' Mark :')           #Use a rangeDef function to check whether the mark is in the range
            
            if mark != STOP_MARKING :                         #If the user typed -1, program won't allow putting the mark in the list
                markList.append(mark)
            
            count += 1

        GradeBook[stdNum] = markList                #Put the list of marks in the dictionary as value for the student number
        

        
    stdNum = str(input('\nEnter next student number (enter end to stop the program):'))
    

printGrade(GradeBook)

            
