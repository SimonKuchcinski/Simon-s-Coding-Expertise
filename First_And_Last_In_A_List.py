#Header
print("This Function will output the first and last elements in a list.")
print('')


#Hard list of elements
numList = ["Fire", 0, 9, "Thought", "Cat", 12]

print("The original list: ",numList)
#Function created to find the first and last element in the list
def GetListFirstLast(paramOrigList):
    
    #Determines first and last elements in the list
    res = [numList[0], numList[-1]]
 
    #Outputs the first and last element in the list
    print("The first and last element of list are: " + str(res))
    print('')
    print("All done.")

#Calls the function to preform the task
print(GetListFirstLast(numList))

