from math import gcd
numbers=list(range(1,3))
lcm= 1
for i in numbers:
    lcm=int(lcm*i/gcd(lcm, i))
print(lcm)