print("Welcome to Number Identifier!")

print("This program will identify if a number that was input is positive, negative, or zero.")

print('')

#obtains the number from the user
integer = float(input("input your number please: "))


print("")

#if condition for a positive outcome
if(integer >= 1):
    print("Your number value is positive")
  
#elif condition for a negative outcome
elif(integer <= -1):
    print("Your number value is negative")

#elif condition for a 0 outcome
elif(integer == 0):
    print("Your number value is 0")
print("")

#end of the program
print("Finished")