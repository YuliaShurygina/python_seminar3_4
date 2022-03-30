# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def create_array(n):
    new_array = []
    for i in range(1, n + 1):
        new_array.append((i,3*i + 1))
    return new_array


array = create_array(6)
print(array)

# Рациональный способ
a = dict([(i, 3*i + 1) for i in range(1, 7)])
print(a)
