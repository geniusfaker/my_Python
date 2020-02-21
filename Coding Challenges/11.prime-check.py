import math
def prime_check():
    num= int(input("Enter a number"))
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            print(str(num)+"is not a prime number")
        else:
            print(str(num)+"is a prime number")
prime_check()
