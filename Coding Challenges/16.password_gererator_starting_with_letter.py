import string
import random
n= int(input("Enter number of Characters for Password:"))
letters=list(string.ascii_letters)
digits=list(range(0,10,1))
special_characters =list(string.punctuation)
characters=letters+digits+special_characters
def password_generator():
    password_1=random.choice(letters)
    password_2=''.join(random.choices(characters, k=n-1))
    password=str(password_1)+str(password_2)
    print(password)
password_generator()
