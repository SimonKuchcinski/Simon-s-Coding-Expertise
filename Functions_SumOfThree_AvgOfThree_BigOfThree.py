#Header
print("Function 1: Gives the sum of three numbers inputted.")
print("Function 2: Gives the average of three numbers inputted.")
print("Function 3: Shows the biggest number out of the three numbers that were inputted.")
print('')

#asks the user to input numbers
paramNum1= float(input("Enter a number: "))
paramNum2= float(input("Enter a number again: "))
paramNum3= float(input("Enter the last number: "))

#function for finding the sum of the three numbers
def SumOfThree(paramNum1, paramNum2, paramNum3):
    #gives the total variable a value in the function
    total= paramNum1 + paramNum2 + paramNum3
    #end of the function and prints the sum of the three numbers
    print("The sum of the numbers entered is: ", round(total,2))

#calls function 1    
print(SumOfThree(paramNum1, paramNum2, paramNum3))


#Function 2 for program 1

#asks the user to input numbers
num1= float(input("Enter a number: "))
num2= float(input("Enter a number again: "))
num3= float(input("Enter the last number: "))

#function for finding the average of the three numbers
def AvgOfThree(num1, num2, num3):
    #gives the total variable a value in the function
    total= num1 + num2 + num3
    #avgTotal variable calculates for finding the average
    avgTotal = total / 3
    #end of the function and prints the average of the three numbers
    print("The average of the set of numbers are: ", round(avgTotal, 2))

#calls function 2
print(AvgOfThree(num1, num2, num3))


#Function 3 for program 1

#asks the user to input numbers
big1= float(input("Enter a number: "))
big2= float(input("Enter a number again: "))
big3= float(input("Enter the last number: "))

#function for finding the largest number of the three
def BigOfThree(big1, big2, big3):
    #defines the large variable using the max function 
    large= max(big1, big2, big3)
    #end of the function and prints the largest number entered
    print("The largest number entered was: ", round(large, 2))

#calls function 3    
print(BigOfThree(big1, big2, big3))

#Program 1

#asks the user to enter three numbers
int1= float(input("Enter a number: "))
int2= float(input("Enter a number again: "))
int3= float(input("Enter the last number: "))

#after the user inputs their numbers the following functions will provide an output
print(SumOfThree(int1, int2, int3))
print(AvgOfThree(int1, int2, int3))
print(BigOfThree(int1, int2, int3))




    