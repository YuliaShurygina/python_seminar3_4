#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from array import array
from pickletools import float8


def integer_array(array):
       int_array = []
       for i in array:
            int_array.append(int(abs(i)))
       return int_array
    
def float_part(array, integer_array):
    float_part_array = []
    for i in range(0, len(array)):
        float_part_array.append(round((abs(array[i]) - integer_array[i]),2))
    return float_part_array
def zero_deletion(array):
    i = 0
    while i < len(array):
        if array[i] == 0:
           array.pop(i)
        else:
           i += 1
    return array


a = [0]
print(f"разница между максимальным и минимальным значением дробной части равна {max(a) - min(a)}")
# if  a != []:
#     b = integer_array(a)
#     print(b)
#     print(float_part(a,b))
#     c = zero_deletion(float_part(a,b))
#     if len(c) == 0:
#         print(f"разница между максимальным и минимальным значением дробной части равна 0")
#     else:
#         print(f"разница между максимальным и минимальным значением дробной части равна {max(c) - min(c)}")        
# else:
#     print("список пустой")
    


