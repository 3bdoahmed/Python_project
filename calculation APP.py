def calc(num1,num2,op): # func to detreman the type of operation and calc it 
    if op == '+': # sum
        return num1+num2
    elif op == '*': # mult
        return num1*num2
    elif op == '/': # div 
        return num1/num2
    elif op == '-': # sub
        return num1-num2
    elif op == '%': # remander
        return num1%num2
    else:
        print("the operation is not found in calc") # if user input error operation

print("Welcome to calc App")
proo = input("please let space betwen number1, process, and number2: ") # get the operation form user
lenn = len(proo) # to Know the size of operation and detrman the end of it 
space = proo.index(" ") # to know when you cleck space
FirstNum = int(proo[0:space]) # the first num =from 0 to index
SecNum = int(proo[space+3 :]) # sec number = from index + 3 to len
operation = proo[space+1] # syntics opertion = index(space)+1

#print (FirstNum)
#print (SecNum)
#print (operation)
result = calc(FirstNum,SecNum,operation) # to call the func and pass the arguments to it 
print("the resulte of operation is =",result) # print the result of operation