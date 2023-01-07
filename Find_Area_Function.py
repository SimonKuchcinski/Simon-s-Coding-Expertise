#Header
print("Welcome to Simon's Find Area Function!")
print("Enter in the desired width and height, and find the area. Thats all there is to it.")
print('')
print('')

#Function 1

#asks the user for the width and height of the desired rectangle
param1= float(input("Please enter the width: "))
param2= float(input("Now enter the height: "))

#function for finding the area of the desired rectangle
def FindArea(param1, param2):
    #variable that multiplies the width and height to find area
    area= param1 * param2
    #end of function 1
    print("The area of the rectangle is", round(area,2))
    print('')
    print("I hope you found this function useful!")

#calls function 1
print(FindArea(param1, param2))

