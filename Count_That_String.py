#Header
print("Welcome to Count That String!")
print("This program will tell you how many characters are in the string. ")
print('')

#Asks the user to input a string
string = input("Please enter a string: ")

#Function created for the program
def CountChar(paramString):

    #Keeps count of characters that are numbers
    numbers = 0
    #Keeps count of characters that are numbers
    letters = 0
    
    #Start of the FOR LOOP
    for char in paramString:
        #Checks for numbers in the string
        if char.isnumeric():
            #adds them
            numbers += 1
        #Checks for letters in the string
        elif char.isalpha():
            #adds them
            letters += 1
    #Outputs the string typed in
    print('String:', paramString)
    #Outputs the number of characters in the string
    print("Characters the string contained:",  letters + numbers)
    print('')
    print("Thank you.")

#Calls the def CountChar(paramString)) function created above
print(CountChar(string))

