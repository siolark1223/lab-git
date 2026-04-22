# Код сгенерирован AI для лабораторной работы №5

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Демонстрация работы AI:")
print(f"Факториал 5: {factorial(5)}")
print(f"Число Фибоначчи 10: {fibonacci(10)}")