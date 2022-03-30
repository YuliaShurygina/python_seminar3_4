#Подсчитать сумму цифр в вещественном числе.
a = -532.12311
def integer_sum(number):
    number = int(number)
    sum = 0
    while number > 0:
        a = number%10
        sum+=a
        number = int(number/10)
    return sum
b = str(a)
b = b.replace('.', '')
b = b.replace('-', '')
print(integer_sum(b))
#Решение с помощью встроенных функций
summa = sum(map(int, str(abs(a)).replace('.', ''))) 
print(summa)