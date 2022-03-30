#Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму
def create_array(n):
    array = []
    for i in range (1, n + 1):
        result = round(((1+1/i)**i),2)
        array.append(result)
    return array
def sum_array(array):
    sum = 0
    for i in array:
        sum+=i
    return sum
new_array = create_array(5)
print(new_array)
#print(sum_array(new_array))
#одной строкой
print(sum((float(i) for i in new_array)))
