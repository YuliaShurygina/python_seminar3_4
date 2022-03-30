#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

def create_array(number):
    new_array = []
    n = 1
    for i in range(number):
        new_array.append(n)
        n*= -3
    return new_array
print(create_array(5))