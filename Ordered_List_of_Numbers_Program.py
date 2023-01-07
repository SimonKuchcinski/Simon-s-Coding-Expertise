print("Hello, welcome to The Ordered List of Numbers Program.")
print('')
print("This program will sort five numbers input by the user. Then it will output the numbers in a list from the lowest to the highest.")
print("Then it will output the numbers in the list one line at a time.")
print("Lastly the program will output the first and last numbers in the list.")
print('')
print("Please enjoy")
print('')


#Asks the user to input any 5 numbers
number1 = input("Please enter a number: ")
number2 = input("Please enter a number: ")
number3 = input("Please enter a number: ")
number4 = input("Please enter a number: ")
number5 = input("Please enter a number: ")

#Creates an empty list
numList = []

#Adds and saves the numbers that were entered into the empty list
numList.append(number1)
numList.append(number2)
numList.append(number3)
numList.append(number4)
numList.append(number5)

#Uses the sort function to organize all the numbers from least to greatest
print(numList.sort())

#Outputs the list of numbers from lowest to greatest
print("The numbers sorted in the list are: ", numList)
print('')

#For statement to print each number one line at a time
for num in numList:
    print(num)
    
#Variable to help print the first and last numbers in the list    
print('')
firstLast = [numList[0], numList[-1]]

#Outputs the first and last number of the list
print("The first and last element of the list are: ", firstLast)

print('')
print("I hope you enjoyed using The Ordered List of Numbers Program.")
