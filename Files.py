#Name: Naon Lee
#Date: August 7, 2018
#purpose: Code a Python program to read input from a text file and save a specific output to another text file

import os


try:
    inputFile = open(os.getcwd() + '/student_mark.txt', mode = 'r')         #open a text file as 'read mode' to read input
           
    outputFile = open('test.txt', 'w')                                      #open another text file as 'write mode' to write output

    stdInfo = inputFile.readline()                                          #save an input by line 
    while stdInfo :
        
        
        stdInfo = stdInfo.split(',')                                        #split the information by comma

        stdNum = stdInfo[0]                                                 #the first factor of a list(information) is the student number
        stdNum = stdNum.rstrip('\n')
        
        total_mark = 0
        
        stdInfo.pop(0)                                                      #remove the first factor(student number)
        
        if len(stdInfo) > 0:
                
            for i in range(len(stdInfo)):                                   #calculate a total mark
                mark = int(stdInfo[i])
                total_mark += mark
            
        outputFile.write('Student Number: ' + str(stdNum) + '\tTotal Marks: ' + str(total_mark) + '\n') #write output in the text file
        
        stdInfo = inputFile.readline()                                      #save an input by line
    

    
except FileNotFoundError:
    print('No such file or directory.')

except KeyboardInterrupt:
    print('You cancelled the operation.')
    
except :
    print('Some I/O error occured')
    
else :
    print("Program is done successfully.")


finally :                               #even the error is occurred, it must operate
    outputFile.close()
    inputFile.close()
