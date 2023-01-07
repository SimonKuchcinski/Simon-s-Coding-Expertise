#Header
print("Welcome to Whats Between 0 to 100, List edition!")
print("This program will take in two numbers that are between 0 and 100.")
print("Then it will output a list of all the numbers that are between the two numbers that were input.")
print("Lastly it will add up all the numbers that are between the two numbers that were input.")
print('')

#asks user for an input
number1= input("Enter the first number between 0 and 100: ")

#asks user for a second input
number2= input("Enter the second number between 0 and 100: ")

#sets a range for the two inputs
input1_input2= range(int(number1), int(number2))

#makes a list of the numbers needed
numberList = list(input1_input2)

#begins the for loop
for num in numberList:
    #outputs the range of numbers between the two given inputs
    print("The numbers in between the two inputs are ", numberList)
    print("")
    #outputs the sum of numbers between the two given inputs
    print("The sum of the numbers between the two inputs is", sum(numberList))
    print("")
    #outputs the total count of numbers between the two given inputs
    print("The count of the inputs in between is", len(numberList))
    print("Your done!")
    break

print('')
print("I hope you enjoyed using Whats Between 0 to 100, List edition.")
