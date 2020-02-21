palindrome= 0
for i in range(100, 999):
    for j in range(100, 999):
        prod = i*j
        if str(prod)==str(prod)[::-1] and prod>palindrome:
            palindrome=prod
print(palindrome)
