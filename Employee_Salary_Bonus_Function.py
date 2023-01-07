#Header
print("This program will take in a salary for an employee, and output the required bonus salary they deserve.")
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
print("The bonus for the employee should be: ","$", findBonus(employeeSal, employeeBonusPerc))
print('')
print("Done")