import random

def player_takes_coins():
    coins_to_take = int(input(f'Human player, how many coins do you take? (1-3): '))
    while coins_to_take < 1 or coins_to_take > 3:
        print('Invalid move! Try again.')
        coins_to_take = int(input(f'Human player, how many coins do you take? (1-3): '))
    return coins_to_take

def computer_takes_coins(coins):
    algorithm = (coins - 1) % 4
    coins_to_take = algorithm or random.randint(1, 3)
    print(f'The computer takes {coins_to_take} coins.')
    return coins_to_take

def coin_game(coins):
    # Initialization
    current_player = 1

    while coins > 0:
        # Print the current state
        print(f'\nCoins remaining: {coins}')

        if current_player == 1:
            # Human player's turn
            coins_taken = player_takes_coins()
        else:
            # computer's turn
            coins_taken = computer_takes_coins(coins)

        # Update the number of coins
        coins -= coins_taken

        # Switch to the next player
        current_player = 3 - current_player  # Alternating between human player and computer
    if current_player == 2:
        current_player = 'Human player'
    else:
        current_player = 'Computer'
    # The player who takes the last coin loses
    print(f'\n{current_player} loses! There are no more coins.')

def main():
    print('''
    "Coin Grab" is a logic game developed in Python, without a graphical interface, where two players compete not
    to be the last one to take the final coin. It starts with a fixed amount of coins, typically 15. On each turn,
    players can take from one to three coins. The player who takes the last coin loses. Challenge your strategy and
    logic to ensure you don't end up with the final coin!
    
    This time you will play against the computer.
    Can you beat it?
    ''')
    # print('You can surrender at any time you want by pressing the key "s".')
    coins = int(input('How many coins do you want to start the game with? '))

    coin_game(coins)

if __name__ == '__main__':
    main()
