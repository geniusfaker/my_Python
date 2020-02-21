list=range(1,11)
squares=[]
for i in list:
    squares.append(i**2)
print(sum(squares))
print(sum(list))
print(-sum(squares)+(sum(list))**2)
    
