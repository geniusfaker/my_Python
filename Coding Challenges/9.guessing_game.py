import random
choice = random.randint(1,9)
player_guess=0
count=0
while player_guess!='exit' and int(player_guess)!= choice:
    player_guess= input("guess a number between 1 and 9 or type 'exit' ")
    if player_guess=='exit':
        break
    else:
        count+=1
        player_guess= int(player_guess)
    if player_guess<choice:
        print("Too low")
    elif player_guess>choice:
        print("Too high")
    else:
        print("perfect" + "you have guessed it in " +str(count)+ "times")
        
    
    
    