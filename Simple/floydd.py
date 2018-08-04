num = int(input("enter the number"))
"""
for i in range (1,num):
    for j in range (1,i+1):
        print (i,end='')
    print ( )

"""
for i in range(1,num):
    for j in range(num-1,i-1,-1):
        print( "*",end='')
    print ()