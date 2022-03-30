#Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1
a = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
b = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
c = ["йцу", "фыв", "ячс", "цук", "йцукен"]
d = ["123", "234", "123", "567"]
e = []
def second_entry(array, n):
    if len(array) == 0:
        return -1
    for i in range(n+1, len(array)):
        if array[i] == array[n]:
            return i
print(second_entry(a, 0))

def presence(array, string):
    if len(array) == 0:
        return -1
    for i in range(len(array)):
        if array[i] == string:
            return i
        else:
            return -1
def second_entry1(array, string):
    if presence(array, string) == -1:
        return "Такого элемента вообще нет!"
    else:
        for i in range(presence(array, string)+1, len(array)):
            if array[i] == string:
                return i   
        return 'второго вхождения строки в список нет'
print(second_entry1(b, "йцу"))
print(second_entry1(c, "йцу"))
print(second_entry1(d, "123"))
print(second_entry1(e, "123"))
