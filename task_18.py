#Реализовать алгоритм перемешивания списка. 
import random
def create_array(number):
    array = []
    for i in range(-number, number +1):
        array.append(i)
    return array
def mix_array(some_array):
    for i in some_array:
       random.shuffle(some_array)
    return some_array
array_1 = create_array(5)
print(array_1)
print(mix_array(array_1))
res = random.sample(array_1, len(array_1))
print(res)


