print('Добро пожаловать в игру Крестики нолики')
print('Введите 2 цифры - номер строки и номер столбца через пробел')
field = [[' '] * 3 for i in range(3)]
def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()
def ask():
    while True:
        hod = input('     Ваш ход: ').split()
        if len(hod) != 2:
            print('Введите 2 точки!')
            continue
        x, y = hod
        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа!')
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона! ')
            continue
        if field[x][y] != ' ':
            print('Клетка занята!')
            continue
        return x, y


def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != ' ':
            print(f"Выиграл {field[a[0]][a[1]]}!")
            return True
    return False
num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win() == True:
        break
    if num == 9:
        print('Ничья')
        break