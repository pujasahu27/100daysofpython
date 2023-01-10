#natural number is a perfect number
def perfect(n):
    x=0
    for i in range(1,n):
        if(n%i==0):
            x+=i
    if(x==n):
        print("perfect number")
    else:
        print("not a perfect number")
        
perfect(6)


    
