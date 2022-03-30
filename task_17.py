#Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
def create_array(number):
    array = []
    for i in range(-number, number +1):
        array.append(i)
    return array
def multiply(array, i, j):
    mult = array[i]*array[j]
    return mult
file = open("file.txt")
index_1 = int(file.readline())
index_2 = int(file.readline())
print(create_array(6))
print(multiply(create_array(6), index_1, index_2))

