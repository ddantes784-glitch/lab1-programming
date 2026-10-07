

# Рекурсивная реализация факториала
def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Итеративная реализация факториала
def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Генерация факториалов от 0 до n
def generate_factorials(n: int) -> list[tuple[int, int]]:
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    result = []
    fact = 1
    for i in range(n + 1):
        if i > 0:
            fact *= i
        result.append((i, fact))
    return result


if __name__ == '__main__':
    # Тесты
    for i in range(11):
        print(f"{i}! = {factorial_recursive(i)}")

    print()

    n = 10
    print(f"Факториалы от 0 до {n}:")
    for num, fact in generate_factorials(n):
        print(f"  {num}! = {fact}")