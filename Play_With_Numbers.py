#Header
print("Welcome to Play With Numbers!")

print("This program will let you input as many numbers as you desire.")

print("When finished inputting your numbers please type done to get results.")

print("The results will give you the amount of numbers entered, the sum of the numbers, and the average of the numbers entered.")

print('')
print('')

#user will input the first number
number= input("Enter your first number: ")

#initialize both variables to 0
count = 0
total = 0

#while loop will check for the kill flag which is "done"
while number != "done":
    #while loop will update variables while the statement is TRUE
    count = count + 1
    total = total + float(number)
    
    #lets user continue to input any number
    number= input("Enter your first number: ")

#variable to calc the average of the numbers that were entered
avg= total / count

#outputs the count of numbers entered 
print("The amount of numbers entered is: ", count)
print("")
#outputs the sum of numbers entered
print("The sum of the numbers entered is: ", total)
print("")
#outputs the average of numbers entered
print("The average of the numbers entered is:", avg)
print("")
#end of the program
print("Your done!")
print("I hope you enjoyed using Play With Numbers!")


