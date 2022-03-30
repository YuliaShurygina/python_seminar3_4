#Строка содержит набор чисел. Показать большее и меньшее число
#Символ-разделитель - пробел
some_string = '68 9 1 -5 52 -12 12'

print(some_string.split())
str = '1234567890'
print(str[2:4])
# def count_numbers(string):
#     count = 0
#     for i in string:
#         if i ==' ':
#             count+=1
#     return count + 1 

# def create_array(string, count):
#     j = 0
#     array = []
#     for i in range (0, count):
#         sub_string = ''
#         if i != count -1:
#             while string[j] != ' '  :
#                 sub_string+= string[j]
#                 j+= 1
#             array.append(int(sub_string))
#             j+=1
#         else:
#             for l in range(j, len(string)):
#                 sub_string+= string[j]
#                 j+= 1
#             array.append(int(sub_string))
#     return array
    
# print(create_array(some_string, count_numbers(some_string)))
# print(max(create_array(some_string, count_numbers(some_string))))
# print(min(create_array(some_string, count_numbers(some_string))))


