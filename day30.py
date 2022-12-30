#factorial
def factorial(n):
    if(n==1 or n==0):
      return 1
    else:
        return(n * factorial(n-1));
n=5;
print("Factorial: ",factorial(n))


#fibonacci series
def fibonacci(n):
     if(n==1 or n==2):
         return 1
     else:
          return(fibonacci(n-1)+fibonacci(n-2))

n=10;
print("Fibonacci: ",fibonacci(n))
       

    



  
