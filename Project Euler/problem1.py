list=[]

for k in range(3, 1000):
    if k%3 ==0 or k%5==0:
        list.append(k)
k+=1
print(sum(list))

