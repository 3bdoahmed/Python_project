# func to calc the salary of employee for spasific houres.
def salary(name, noHoures):
    salary_rate = 500 # slary per one houre
    total = salary_rate * noHoures # clc the total salary per spasific houres.
    print(name + "get the salary " + str(total)+ " pount when workes for "+ str(noHoures))



# get the name and the number of houres that the employee works
employeeName = input("please enter employee's name: ")
employee_no_of_houre = int(input("please enter the nuber of houre employee workes: "))

# call the func salary.
salary(employeeName,employee_no_of_houre)