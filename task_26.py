#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
def Fibonacci(n):
    if n==1 or n==2:
        return 1
    elif n == 0:
        return 0
    else:
        return  Fibonacci(n - 1) + Fibonacci(n - 2)
def nega_fibonacci(n):
    if n == -1:
        return 1
    elif n == -2: 
        return -1
    else:
        return nega_fibonacci(n+2) - nega_fibonacci(n+1)
def create_array(n):
    fibonacci_array = []
    for i in range (-n, 0):
        fibonacci_array.append(nega_fibonacci(i))
    for i in range (0, n + 1):
        fibonacci_array.append(Fibonacci(i))
    return fibonacci_array

print(create_array(8))