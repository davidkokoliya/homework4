def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка'))
        bonus = int(input('Премия'))
        res = time * salary + bonus
        print(f'Заработная Плата Сотрудника  {res}')
    except ValueError:
        return print('Not a number')
sal()