#Header
print("This program will take in a salary for an employee, and output the required bonus salary they deserve.")
print("NOTE: You can input as many employee ID's as needed.")
print("Input ""quit"" when asked for employee ID to finish. The output will display the emp total, bonus total, and the bonus avg.")

print('')

#Lets user input the wanted employee salary
employeeSal = float(input("Please enter your salary: $"))

#Lets user input the wanted bonus percent for the employee
employeeBonusPerc = float(input("Enter the bonus percentage: "))

#Function created to calc the employeeSal and employeeBonusPerc
def findBonus(paramSalary, paramBonusPercent):
    
    #Converts the percentage into a decimal
    bonusPercent = float(paramBonusPercent) / 100
    
    #Multiplies the new decimal by the salary
    bonusTotal = float(paramSalary) * float(bonusPercent)
    
    #returns the answer
    return bonusTotal

#Calls the function and provides the output
print("The bonus for the employee should be: ","       $", findBonus(employeeSal, employeeBonusPerc))


#***********************************************************************************************************************************************************


#Asks the user to input employee ID
employeeID = input("Please enter employee ID: ")

#Created empty lists and initializing variables to zero to start
IDList = []
salaryList = []
bonusPercList = []
BonusAmtList = []
employeeCount = 0
employeeTotalBonus = 0
avgBonus = 0

#While loop created if the user inputs quit when asked for the empID then the loop will stop
while(employeeID != "quit"):
    
    #Asks the user to input the employee salary if quit was not entered
    salary = input("Please enter the salary of the employee: ")
    
    #Asks the user to input the bonus percentage for the employee if quit was not entered
    bonusPerc = input("Please enter the bonus percentage: ")
    
    #Adds and saves all the inputs to the empty lists
    IDList.append(employeeID)
    salaryList.append(salary)
    bonusPercList.append(bonusPerc)
    
    #Calls my function that was designed in project 2a to calculate the bonus
    empBonus = findBonus(float(salary), float(bonusPerc))
    
    #Adds and saves the bonus amount to the BonusAmtList
    BonusAmtList.append(empBonus)
    
    #Tracks the employee count
    employeeCount = employeeCount + 1
    
    #Calculates the total bonus of all employees
    employeeTotalBonus = employeeTotalBonus + empBonus
    
    #Calculates the total average of all the employee bonus that was given
    avgBonus = employeeTotalBonus / employeeCount
    
    #Outputs the message below
    print("Employee ID | Employee Salary | Employee Bonus Percentage | Employee Bonus")
    
    #For loop that tracks the length of all the lists
    for employee in range(len(IDList)):
        
        #Outputs the updated lists after the user inputs the employee bonus percentage
        print(IDList[employee], '         ',salaryList[employee],'           ', bonusPercList[employee],'                           ', BonusAmtList[employee])
    
    #While loop starts again asking for another Employee ID
    employeeID = input("Please enter employee ID: ")


#Else statement created when the user inputs the kill flag
else:
    
    #Outputs the message below
    print("Employee Total | Bonus Total | Bonus Avg. ")
    
    #For loop that tracks the length of all the lists
    for employee in range(len(IDList)):
        
        #Outputs the total number of employees and the total bonus of all the employees and the average of all the bonuses
        print(employeeCount,'              ', employeeTotalBonus,'        ',avgBonus)