from random import randint

print('=' * 35)
print('{:^35}'.format('Tafer s Odds or Evens'))
print('=' * 35)
victories = pc = player = 0
while True:
    while True:
        try:
            player = int(input('Choose a number between 0 to 10:'))
            if not 0 <= player <= 10:
                raise ValueError("Invalid option!")
        except ValueError as e:
            print("Invalid option. Just numbers from 0 to 10!")
        else:
            break
    choice = str(input('Odds or Evens [O/E] ?')).upper().strip()[0]
    while choice not in 'OE':
        choice = str(input('Invalid option! Odds or Evens [O/E] ?')).upper().strip()[0]
    pc = randint(1, 10)
    sum1 = pc + player
    if choice == 'O':
        print('You chose Odds!\nTafer chose Evens!')
    elif choice == 'E':
        print('You chose Evens!\nTafer chose Odds!')
    print(f'You put {player} and Tafer put {pc}!\nTotal: {sum1}!')
    if sum1 % 2 == 0:
        print('Evens!')
    else:
        print('Odds!')
    if choice == 'E' and sum1 % 2 == 0:
        print('You win!')
        print('Let s play again...')
        victories += 1
    elif choice == 'O' and sum1 % 2 != 0:
        print('You win!')
        print('Let s play again...')
        victories += 1
    elif choice == 'E' and sum1 % 2 != 0:
        print('You lose!')
        break
    elif choice == 'O' and sum1 % 2 == 0:
        print('You lose!')
        break
if victories == 0:
    print(f'GAME OVER.\nYou haven t defeated Tafer once!')
elif victories == 1:
    print(f'GAME OVER.\nYou defeated Tafer one time!')
elif victories > 1:
    print(f'GAME OVER.\nYou defeated Tafer {victories} times!')
