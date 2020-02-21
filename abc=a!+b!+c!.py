import math

for a in range(6):
    for b in range(6):
        for c in range(6):
            if (a*100 +b*10+ c == math.factorial(a) +math.factorial(b) +math.factorial(c)):
                print(a*100 +b*10+ c)
    
        