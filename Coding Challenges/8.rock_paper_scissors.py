choice=['rock', 'paper', 'scissors']
while True:
    for i in range(len(choice)):
        print(str(i) +':' +choice[i])
    p1_choice=int(input('enter a choice:'))
    p2_choice=int(input('enter a choice:'))
    dif=p1_choice - p2_choice
    if dif==0:
        print("it is a draw")
    elif dif==1 or dif==-2:
        print("player 1 wins")
    else:
        print("player 2 wins")
    
    play_again=str(input("play again:hit 'y' for yes and 'q' for quit"))
    if play_again=='y':
        continue
    else:
        print("Thankyou for playing")
        
        break
    