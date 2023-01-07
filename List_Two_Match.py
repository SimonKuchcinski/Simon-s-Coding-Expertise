#Header
print("Welcome to List Two Match!")
print("Type in a list of your choosing. Then another list of your choosing, and see if they match.")
print('')

#Asks the user to input elements for the first list
input1 = input("Please enter some elements for list 1: ")

print('')

#Asks the user to input elements for the second list
input2 = input("Please enter some elements for list 2: ")

#Creates a empty list
list1 = []

#Creates a second empty list
list2 = []

#Saves the elements in list1
list1.append(input1)

#Saves the elements in list2
list2.append(input2)

#Function created to compare lists to see if they are the same
def CompareLists(paramList1, paramList2):
    
    #IF statement if lists are the same
    if list1 == list2:
        print("These two lists are the same!")
        
    #Else condition if lists are not the same
    else:
        print("These two lists are different!")
    
    print('')
    
    print("I hope you enjoyed using List Two Match!")
#Calls the function created above        
print(CompareLists(input1, input2))
        