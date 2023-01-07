#Header
print("This program will combine two lists that the user will input, and output them in one big list.")
print("When finished entering the elements in both lists, input ""done"" to finish.")
print('')


numInput = int(float(input("Please enter a number or a string: ")))

#Created function for program #3
def GetNewNumberList(num):
    #Asks the user to input a number

    #Creates an empty list
    numList = []
    #Creates an empty list
    newNumList = []
    #Sets the count of the list to zero
    count = 0
    
    #While loop begins excepting other numbers to each of the two list until user enters kill flag
    while (num != "done"):
        #If done is not entered then program asks for another number for the new list
        newNum = str(input("Please enter a number or a string for the new list: "))
        #Adds and saves numbers in the numList
        numList.append(num)
        #Adds and saves numbers in the newNumList
        newNumList.append(newNum)
        #Keeps count of numbers in the list
        count = count + 1
        #Keeps the while loop going and asks again for a number until kill flag is entered
        num = str(input("Please enter a number or a string: "))
    
    
    #Tracks both of the lists values
    listCount = 0
    
    #For loop begins and tells program where the numbers go
    for dig in numList:
        #Outputs each list side by side of one another
        print("List of all the elements", numList[listCount], newNumList[listCount])
        #Keeps track of the numbers in both lists
        listCount = listCount + 1
        #Creates a new variable to display all the lists in one single list
        finalList = numList + newNumList

    #Outputs all the numbers in both lists into a single list
    print("The final list of all the elements is: ", finalList)
    print('')
    print("I hope you enjoyed!")

print(GetNewNumberList(numInput))

