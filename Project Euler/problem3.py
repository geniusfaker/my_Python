a=range(998001, 10000)

for i in a:
    list=[];
    b=str(i)
    if b== b[::-1]:
        list.append(i)
print(list)
        