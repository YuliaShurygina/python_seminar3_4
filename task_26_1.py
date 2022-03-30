def fib(n):
    if n == 0: return 0
    elif n == 1 or n ==2:  return 1
    if n >0:
       return fib(n-1) + fib(n-2)
    else:
       return int((-1)**(n+1)*fib(-n))
n = 8
def create_fibo_list(n):
   fibo_list = []
   for i in range(-n, n +1):
      fibo_list.append(fib(i))
   return fibo_list
print(create_fibo_list(n))
    

