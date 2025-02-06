
def calculator(calc):
    try:
        tokens = calc.split()
        if len(tokens)!= 3:
            raise ValueError('Неверный формат ввода! Необходимо ввести например: (a + b, a - b, a * b, a / b.)')

        a, op, b = tokens

        a = int(a)
        b = int(b)
        if not (1 <= a <= 10) or not (1 <= b <= 10):
            raise ValueError('Числа должны быть от 1 до 10 включительно!')

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '/':
            result = a // b
        elif op == '*':
            result = a * b
        else:
            raise ValueError('Неподдерживаемая арифметическая операция!')

        return result

    except:
            print ('Ошибка!')
            exit()


calc = input ('Введите выражения из представленного примера: (a + b, a - b, a * b, a / b.)')
result = calculator(calc)
print(f"Результат: {result}")
