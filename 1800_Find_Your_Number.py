#Header
print("Hello, and welcome to 1-800 Find Your Number!")
print('')

#Function 1

#asks the user to input a 1-800 number
transNum= str(input("Please enter a 1-800 number in letter format to translate into numbers. Do not include hyphens: "))

#function to translate letters into numbers
def Translation(transNum):
    
    #sets the number variable to check for a string
    number= ''
    
    #start of a for loop that sets the string to a number 
    for str in transNum:
        for i in range (len(str)):
            if str[i] in 'ABC':
                number= number + '2'
            elif str[i] in 'DEF':
                number= number + '3'
            elif str[i] in 'GHI':
                number= number + '4'    
            elif str[i] in 'JKL':
                number= number + '5'
            elif str[i] in 'MNO':
                number= number + '6'
            elif str[i] in 'PQR':
                number= number + '7'
            elif str[i] in 'STUV':
                number= number + '8'
            elif str[i] in 'WXYZ':
                number= number + '9'
    
    #end of the for loop
    print("The correct translation is:", "1800", number)
    print('')
    print("Thank you, and have a great day!")

#calls function 1
print(Translation(transNum))





        
                
