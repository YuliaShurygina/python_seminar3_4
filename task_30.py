#Вычислить число pi  c заданной точностью d
#	Пример: при d = 0.001, pi = 3.141. 10-1d10-10

accuracy = int(input("Введите точность определения числа пи(количество знаков после запятой) от 1 до 10 : "))
def find_pi(a):
    if a < 1 or a > 10:
        return "Точность задана неверно. Попробуйте еще раз"
    pi_control = round(3.14159265359, a)
    pi = 0
    count = 0
    i = 1
    while round(pi, a) != pi_control:
        if count % 2 == 0:
            pi += 4*(1 / i)
        else:
            pi -= 4*(1 / i)    
        i += 2
        count += 1
    return (pi, count)
print(find_pi(accuracy))
