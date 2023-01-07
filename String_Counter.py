#Header
print("Welcome to String Counter!")
print('')

#Prompts the user to input words
string = str(input("Please enter the words you wish: "))

#Function created to count words
def CountWords(paramString):
    
    #Variable created that uses len to count the words, and the split function to seperate words from each other
    countString = len(string.split())
    
    #Returns the total
    return countString

#Outputs the number of words that were inputted
print(f"the amount of words in your string is: {CountWords(string)}")
print('')
print("All Done!")
        
        
    
            
        

