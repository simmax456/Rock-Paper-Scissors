import random

while True:
    print('Rules\nR wins S\nP wins R\nS wins P\n')
    print('Enter "R for Rock", "P for Paper", or "S for Scissors"\n')
    plays = ['R', 'P', 'S']

    computer = random.choice(plays)
    player = input('Enter selection: ')

    if player in plays:
        print(f'Player played "{player}" : CPU played "{computer}"')

        if player == 'R' and computer == 'S':
            print('Rock smashes scissors! You win!')
            break

        elif player == 'P' and computer == 'R':
            print('Paper covers rock! You win!')
            break

        elif player == 'S' and computer == 'P':
            print('Scissors cuts paper! You win!')
            break

        elif player == computer:
            print(f"You both selected {player}. It's a tie!")
            play_again = input('Play again? (y/n): ')
            if play_again.lower() != 'y':
                break
        else:
            play_again = input('You lose, wanna play again? (y/n): ')
            if play_again.lower() != 'y':
                break
    else:
        print('Invalid input! Enter again\n')