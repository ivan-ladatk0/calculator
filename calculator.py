what = input ('что выполнить? (+, -, /, *):')

a = float (input('Введите первое число:'))
b = float (input('Введите второе число:'))

if not (1 <= a <= 10) or not (1 <= b <= 10):
    raise ValueError("Числа должны быть от 1 до 10 включительно.")


if what == '+':
    c = a + b
    print('Результат:' + str (c))
elif what == '-':
    c = a - b
    print('Результат:' + str (c))
elif what == '/':
    c = a / b
    print('Результат:' + str (c))
elif what == '*':
    c = a * b
    print('Результат:' + str (c))
else:
    print('Неверное значение')



