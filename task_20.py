#Определить, присутствует ли в заданном списке строк, некоторое число 
some_array = ['first1', 'second2', 'third3', 'fourth', 'fifth5', 'sixth', 'seventh7']
def presence(array, number):
    number = str(number)
    for i in array:
        for j in i:
            if j == number:
                return True
    return f'Число {number} отсутсутствует'
print(presence(some_array, 2))