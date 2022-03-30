#Найти корни квадратного уравнения Ax² + Bx + C = 0
#Математикой
#Используя дополнительные библиотеки*
import Mathf
def squares(a,b,c):
    if a == 0:
        return round(-c/b, 2)
    D = b**2 - 4*a*c
    if D < 0:
        b1 = round(-b/2*a,1)
        d = round(Mathf.sqrt(-D)/2*a,1) 
        return f"действительных корней нет. Комплексные корни: {b1} - {d}*i, {b1} + {d}*i"
    elif D == 0:
        return round(-b / 2*a, 2)
    else:
        return (round((-b + Mathf.sqrt(D))/2*a, 2), round((-b -Mathf.sqrt(D))/2*a, 2))
print(squares(1, 4, 6))