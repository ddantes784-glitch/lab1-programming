# Ввод чисел
a = float(input())
b = float(input())
c = float(input())
# Ср. значение
average = (a + b + c) / 3
# минимум
minim = min(a, b, c)
# макс
maximum = max(a, b, c)
print(f'Среднее арифметическое: {average:.2f}')
print(f'Минимум: {minim}')
print(f'Максимум: {maximum}')