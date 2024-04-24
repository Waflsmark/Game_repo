from random import randint
    
SIZE_N = 5
SIZE_M = 5

char_x = randint(0, SIZE_N - 1)
char_y = randint(0, SIZE_M - 1)
char_sign = 'X'

exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)

enemy_x = randint(0, SIZE_M - 1)
enemy_y = randint(0, SIZE_M - 1)
enemy_sign = 'Z'

fight_num1 = randint(0, 10)
fight_num2 = randint(0, 10)
fight_num3 = randint(0, 10)

right_fight_answer = fight_num1 + fight_num2 * fight_num3

turns = 0

while True: 

    world_map =''
    win_condition = char_x == exit_x and char_y == exit_y
    fight_condition = char_x == enemy_x and char_y == enemy_y

    if win_condition: 
        char_sign = 'W'

    for j in range(SIZE_M):

        row = '|'

        for i in range(SIZE_N):

            if char_x == i and char_y == j:
                row += f'{char_sign}|'
            elif exit_x == i and exit_y == j:
                row += 'O|'
            elif enemy_x == i and enemy_y == j:             
                row += f'{enemy_sign}|'
            else:
                row += ' |' 

        world_map += f'{row}\n'

    print(world_map)

    if win_condition:
        print(f'!You WON in {turns} turns!')
        break
    
    if fight_condition:
        fight_answer = int(input(f'Enter the answer to {fight_num1} + {fight_num2} * {fight_num3} = '))
        if fight_answer == right_fight_answer:
            print('You killed an enemy')
            enemy_sign = 'K'
        else:
            print('You`re killed by enemy')
            print('YOU DIED')
            break

    direction = input('Enter direction (u / d / l / r): ')

    if direction == 'u' and char_y > 0:
        char_y -= 1
    elif direction == 'd' and char_y < SIZE_M - 1:
        char_y += 1
    elif direction == 'l' and char_x > 0:
        char_x -= 1
    elif direction == 'r' and char_x < SIZE_N - 1:
        char_x += 1

    turns += 1