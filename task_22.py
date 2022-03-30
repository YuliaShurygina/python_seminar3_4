#Найти сумму чисел списка стоящих на нечетной позиции
def sum_odds_indexes(array):
    sum = array[1]
    for i in range (3, len(array)):
        if i % 2 != 0:
            sum += array[i]
    return sum
print(sum_odds_indexes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))