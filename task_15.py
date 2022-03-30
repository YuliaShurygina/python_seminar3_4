#Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]
def create_array(N):
    array = []
    n = 1
    for i in range (1,N+1):
        n*=i
        array.append(n)
    return array
print(create_array(4))


       