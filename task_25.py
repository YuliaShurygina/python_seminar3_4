#Написать программу преобразования десятичного числа в двоичное

from array import array


def binary(number):
    bin_arr = []
    while number>= 2:
        bin_arr.append(int(number % 2))
        number = int(number/2) 
    if number == 1:
        bin_arr.append(1)
    return bin_arr

def reverse(array):
    reverse_arr = []
    for i in range(0, len(array)):
        reverse_arr.append(array[len(array)-i-1])
    return reverse_arr
print(''.join(str(i) for i in reverse(binary(77))))

