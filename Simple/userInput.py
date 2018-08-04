#Import Addition from sum
def sum(num1,num2):
    return num1 + num2

def minus(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def mod(num1,num2):
    return num1%num2

def divide(num1,num2):
    return num1/num2

a=int(input("enter the number"))
b=int(input("enter the number2"))
c=input("enter your choice")

if c=='1':
    #val=sum(a,b)
    print(sum(a,b))
elif c=='2':
    print(minus(a,b))
elif c=='3':
    print(multiply(a,b))
elif c=='4':
    print(mod(a,b))
elif c=='5':
    print(divide(a,b))
else:
    print("please enter valid choice")