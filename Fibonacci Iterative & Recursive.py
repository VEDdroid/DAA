'''Fibonacci Iterative'''

print("How many numbers you want to print ?")
tNum = int (input())
num1,num2,count= 0 ,1 ,0

if (tNum == 0):
    print("Valid Number")
    
elif (tNum == 1):
    print(num1)
    
else:
    while(count< tNum):
        print(num1, end=" ")
        c = num1 + num2
        num1 = num2
        num2 = c
        count += 1
        
        
        
''' Fibonacci Recursive
        
def fib (n):
    
    if (n <= 1):
        return n
    
    else:
        return fib(n-1)+fib(n-2)
        

print("How many numbers you want to print ?")
n = int (input())

for i in range (n):
    print(fib(i), end= " ") 
    '''