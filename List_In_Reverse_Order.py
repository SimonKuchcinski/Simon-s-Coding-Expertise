#Header
print("This program outputs the reversed order of the given list.")
print('')

#List containing the elements needing to be reversed
origList = ["Cat", 6, 59,"Apple", 0, "Food"]

print("The original list: ",origList)
print('')


#Function created to reverse a given list
def ReverseList(paramOrigList):
    #Tells program to preform the reverse function for the list of given elements
    origList.reverse()
    
    
    #Outputs the list in reversed order
    print("The list in reverse order is: ", origList)
    print('')
    print("All done.")

#Calls the function and can be used freely. 
print(ReverseList(origList))

