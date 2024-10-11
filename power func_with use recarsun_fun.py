#----------->> by use recrgan function.
def pow(baseNUm, powwrNUM):
    if powwrNUM == 1 :
        return baseNUm
    else:
        return baseNUm*pow(baseNUm,powwrNUM-1)

base_num = input("please enter base number: ")
power_num = input("please enter power number: ")
print("the result power number "+ base_num +" of number "+ power_num +" equal ",pow(int(base_num),int(power_num)))

#---------------->> by use for loop
#def pow(baseNum, powerNum):
#    result=1
#    for index in range(powerNum):
#        result*= baseNum
#    return result  
#print(pow(2,2))



