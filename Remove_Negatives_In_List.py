#Header
print("This function will take a list, and output the list with no negative numbers.")
print('')

#Hard list of elements
listOfNum = [11, -21, 0, 45, 66, -93]


print("The original list: ",listOfNum)
#Function created to delete negatives in a list
def DeleteNegatives(paramList):
    
    #For loop that iterates each element in the list
    for x in listOfNum:
 
        #checks if the element is a negative number or not
        if x > 0:
            
            #Outputs only numbers in the list that are not negatives
            print([x], end=" ")
    #Outputs the message below
    print(":is the list with no negatives")
    print('')
    print("Finished.")

#Calls the function for use anytime
print(DeleteNegatives(listOfNum))
