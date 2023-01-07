#Header
print("This program will tell the user how many negative numbers are in a list.")
print('')

testList = [-5, -7, 10, 28, -62, 45, -11]
  
#Created function for the program
def CountNegatives(paramOrigList):
    #Sets the negative count to zero 
    negCount = 0
 
    #For loop begins for the paramOrigList
    for num in paramOrigList:
    
        #Makes sure the number in the list is less then zero
        if num <= 0:
            #Adds 1 counter for each negative that was found in the list
            negCount += 1
    
    print(testList)
    #Outputs the total of negative numbers in the list        
    print("Negative numbers in the list: ", negCount)
    print('')
    
    print("Finished")

print(CountNegatives(testList))




