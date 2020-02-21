a,b=1,2
list=[]
while a<4000000:
    a, b= b, b+a
    if a%2==0:
        list.append(a)
print(sum(list))
    