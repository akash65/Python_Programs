
def sum(num1,num2):
    return num1+num2
    

def minus(num1,num2):
    return num1-num2
   

def divide(num1,num2):
    if num2 == 0:
        print("divide by zero")
    else:
        return num1/num2
        


def multiply(num1,num2):
        return num1*num2
       


x = int(input("enter the value1:"))
y = int(input("enter the value2:"))

choice = int(input("enter the choice:"))
if choice == 1:
    print(sum(x,y)) 

elif choice == 2:
    print(minus(x,y))

elif choice == 3:
    print(divide(x,y))

elif choice == 4:
    print(multiply(x,y))

else:
    print("choice not found")

    

