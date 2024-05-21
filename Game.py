print('Rock')


print('Paper')

print('Scissors')


player1 = input('player 1.Make Your Move ')


player2 = input('player 2.Make Your Move ')


if player1 == 'rock' and player2 == 'player':
    print('player 1 wins')

elif player1 == 'rock' and player2 == 'scissors':
    print('player 2 win')

elif player1 == 'rock' and player2 == 'paper':
    print('player 2 win')

elif player1 == 'rock' and player2 == 'rock':
    print('player 1 win')
elif player1 == 'rock' and player2 == 'rock':
    print('player 1 win')


elif player1== player2:
    print('its a lie')

else:
    print('something went wrong')    
    