'''
    Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
The program should work as follows:
1. When the program begins, a random number in the range of 1 through 3 is generated. If the number is 1, then the computer has chosen rock.
If the number is 2, then the computer has chosen paper. If the number is 3, then the computer has chosen scissors. (Don’t display the computer’s choice yet.)

2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.

3. The computer’s choice is displayed.

4. A winner is selected according to the following rules:
• If one player chooses rock and the other player chooses scissors, then rock wins.   (Rock smashes scissors.)
• If one player chooses scissors and the other player chooses paper, then scissors   
  wins. (Scissors cuts paper.)
• If one player chooses paper and the other player chooses rock, then paper wins.
  (Paper wraps rock.)
• If both players make the same choice, the game must be played again to determine the winner.

'''
import random as rd

def main():

    #taking user input
    
    user_choice=input("Enter your choice (rock, paper,scissor: )")

    #call computer_choice to genrate a comptuer ans

    computer_choice=computer_output()

    #calling a win_condtion  function to check who won the game 

    winner=win_condtion(user_choice,computer_choice)

    # condtion to handle an eror that have ocurred
    
    if winner=='404':
        return
    

    print(f'computer choice {computer_choice}')


    # print who have won the game
    
    if winner==user_choice:
        print('user wins!')

    else:
        print('computer wins! ')

    #if user want to continue the game or 

    x=input('Do you want to play again:?(yes/no): ')
    if x=='yes' or x=='y':
        main()
    else:
        print("wrong input ?")
    
    
            

# function to genrate  a computer input

def computer_output():
    choices=['rock','paper','scissor']
    return choices[rd.randint(0,2)]


#checking win conditoin on basic of rules
'''
• If one player chooses rock and the other player chooses scissors, then rock wins.   (Rock smashes scissors.)
• If one player chooses scissors and the other player chooses paper, then scissors   
  wins. (Scissors cuts paper.)
• If one player chooses paper and the other player chooses rock, then paper wins.
  (Paper wraps rock.)
• If both players make the same choice, the game must be played again to determine the winner.

'''


def win_condtion(x,y):
    if x==y:
        print("it's a tie !")
        print('its a tie ! play agian')
        main()
    elif x=='rock'  and y=='scissor':
        return(x)
    elif x=='rock' and y=='paper':
        return(y)
    elif x=='paper' and y=='rock':
        return(x)
    elif x=='paper' and y=='scissor':
        return(y)

    elif x=='scissor' and y=='rock':
        return(y)
    elif x=='scissor' and y=='paper':
        return(y)
    else:
        print(f'some thing went wron contact the developer {x,y}')
        return('404')
 

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return None  # It's a tie
    elif (
        (user_choice == 'rock' and computer_choice == 'scissor') or
        (user_choice == 'scissor' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'user'
    else:
        return 'computer'       
        
    
#call main body

if __name__=="__main__":
    print('Lets play Rock,Paper,Scissors !')
    main()
