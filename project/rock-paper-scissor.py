import random


def doPlay():

    choice = ['R','P','S']
    user = input(f'Player A : (What do you choose ? {choice} )')
    computer = random.choice(choice)

    user = user.upper()
    computer = computer.upper()

    if( user not  in choice ):
        print ('Wrong input')
        return None

    print(f'Player B : {computer}') 

    if(user==computer):
        return 'It is a tie :-|'

    if(is_user_win(user,computer)):
        return 'You won :-) '
    
    return 'You lost :-( '



def is_user_win(u,c):

    # R > S ,  S > P ,  P > R

    if ( (u == 'R' and c == 'S') or (u == 'S' and c == 'P') or (u == 'P' and c == 'R')  ):
        return True

a = 0
while a < 10:
    print(doPlay())
    a += 1