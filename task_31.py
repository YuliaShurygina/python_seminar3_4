#Составить список простых множителей натурального числа N
def simple_multiplier(number):
    array_simple_multipliers = []
    for i in range (number - 1, 1, -1):
        if number % i == 0:
            count = 0
            for j in range (i - 1, 1, -1):
                if i % j == 0:
                    count+= 1
            if count == 0: 
                array_simple_multipliers.append(i)
    return array_simple_multipliers
print(simple_multiplier(52))