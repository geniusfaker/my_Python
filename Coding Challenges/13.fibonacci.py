a= int(input("enter starting number:")) 
b=int(input("enter starting number:"))
count= int(input("enter how many numbers to generate:"))

def fibonacci(a,b,count):
   fibonacci_list =[a, b]
   for i in range(count-2):
       b=a+b
       a=b
       fibonacci_list.append(b)
   print(fibonacci_list)        
fibonacci(a,b,count)