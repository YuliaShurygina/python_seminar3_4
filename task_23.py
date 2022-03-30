#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
from array import array


def multiplay(array):
    multiplay_array = []
    length = len(array)
    if length % 2 !=0:
        length = int(len(array)/2 + 1)
    else:
        length = int(len(array)/2)
    for i in range(0, length):
        multiplay_array.append(array[i]*array[len(array)-i-1])
    return multiplay_array
   
print(multiplay([2, 3, 4, 5, 6]))
print(multiplay([2, 3, 5, 6]))