#Header
print("Welcome to My Simple Math Program!")
print('')
print("This program will let a user input one number that is less then 500, and divide it by a second number the user will have to input.")
print('')

#asks user to enter an integer
number1= int(input("Please enter an integer that is less than 500: "))

#while loop continues if the first integer is less then 500
while number1 < 500:

    
    #if number is less then 500 then the user inputs the second number
    number2= int(input("Pleae enter the second number you want to divide by: "))
    print('')
   
    #variable that divides number1 and number2 to find the answer
    number3= number1 / number2
    print(number3)
    break

#while loop if the first integer is greater then 500
while number1 > 500:
    print("Dude this number is waaay to high, try again!")
    number1= int(input("Please enter an integer that is less than 500: "))
    
    number2= int(input("Pleae enter the second number you want to divide by: "))
    print('')
    
    number3= number1 / number2
    print(number3)
    break

print('')
print("Awesome you are now done!")
print("I hope you enjoyed!")

