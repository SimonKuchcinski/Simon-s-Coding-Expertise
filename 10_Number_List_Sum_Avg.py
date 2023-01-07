#Header
print("Welcome, this program will let you input 10 Numbers, and will output them back in a list. Along with the sum, and average of the 10 numbers.")
print('')

#Asks the user to enter a number
value1= int(input("Please enter a integer to start your list: "))

#Makes an empty list for the numbers
valueList = []
#Adds the first number to the list
valueList.append(value1)
        
#For loop that lets the user enter in 9 more numbers using the range function        
for value1 in range(9):
    #Asks the user to enter a number
    value2= int(input("Please enter another integer for the list: "))
    #Adds the numbers to the list one by one 
    valueList.append(value2)

#Outputs the list of numbers entered
print(valueList)
#Outputs the sum of the list of numbers
print("The sum of the numbers in the list is:", sum(valueList))
#Outputs the average of the list of numbers
print("The average of the numbers in the list is:", sum(valueList) / 10)
print('')
print("I hope you enjoyed using this program!")