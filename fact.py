num=int(input("here the number"))

fact = 1

if num ==0:
    print("it is not fact number")
if num >1:
    for i in range(1,num+1):
        
        fact = fact *1
        print(fact)