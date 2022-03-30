#Найти НОК двух чисел
from array import array


def dividers(number):
    array_dividers = []
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            array_dividers.append(i)
    return array_dividers
def biggest_divider(array1, array2):
    for i in array1:
        for j in array2:
            if j == i:
                return j
def smallest_general_multiply(number1, number2, divider):
    return number1*number2/divider
    
print(dividers(42))
print(dividers(24)) 
print(biggest_divider(dividers(24), dividers(42)))
print(smallest_general_multiply(24, 42, biggest_divider(dividers(24), dividers(42))))
