#Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел


from datetime import datetime
def create_array(number, length):
    array = []
    m = number - 1
    if m == 0:
        m = m -1
    c = m - 1
    a = m - 2
    for i in range(0, length):
        item = (a*number +c)%m
        array.append(item)
        number = item
      
         
    return array

t = datetime.now()
print(t.strftime("%I:%M:%S"))
s = int(t.strftime("%S"))
print(s)
print(create_array(s, 10))