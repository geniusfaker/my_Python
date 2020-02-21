import random
def compare_numbers(num, user_num):
    cows_bulls=[0,0]
    for i in range(len(num)):
        if num[i]==user_num[i]:
            cows_bulls[0]+=1
        elif num[i] in user_num:
            cows_bulls[1]+=1
    return cows_bulls
if __name__=="__main__":
    playing=True
    num=str(random.randint(1000, 9999))
    guesses=0
    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every correct number in the wrong place, you get a bull. For every correct number in the right place, you get a cow.")
    print("The game ends when you get 4 cows!")
    print("Type exit at any prompt to exit.")
   
    while playing:
        user_num=input("Enter best guess")
        if user_num=='exit':
            break
        count=compare_numbers(num, user_num)
        guesses+=1
        
        print("You have "+ str(count[0]) + " cows, and " + str(count[1]) + " bulls.")

        
        if count[0]==4:
            playing=False
            print("You won the game in " + str(guesses) + " \n The number was "+str(num))
            break #redundant exit
        else:
            print(" try again.")