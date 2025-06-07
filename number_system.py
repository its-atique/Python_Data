"""num1=  300
num2=400
num3=403

if (num1 >num2) and (num1> num3):
    print(num1,"It is greaternumber")
    
elif (num2 >num1) and (num2> num3):
    print(num2, "it is the greater number")
    
else:
    print(num3, "it is greater number")
    
    """
    
num= int(input("please enter a number"))

if num <= 1:
    print("it is not prime number")
    
else:
    for i in range (2,num):
        if num %i ==0:
            print("not prime")
            break
       
        else:
            print("prime")
    
    
    