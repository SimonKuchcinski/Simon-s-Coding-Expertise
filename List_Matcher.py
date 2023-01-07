#Header
print("Welcome to List Matcher")
print("This program will tell if a list has the same elements or not.")
print('')

#Asks the user to input elements in list1 and list2
input1 = input("Please enter some elements for list 1: ")
input2 = input("Please enter some elements for list 2: ")

#Empty list1
list1 = []

#Empty list2
list2 = []

#Saves elements to both lists
list1.append(input1)
list2.append(input2)

#Function created to see if both lists are the same or not
def CompareLists(paramList1, paramList2):
    if list1 == list2:
        print("These two lists are the same!")
        
    else:
        print("These two lists are different!")

#Calls the function above    
print(CompareLists(input1, input2))
        