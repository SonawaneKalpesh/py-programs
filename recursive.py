def fun(n):
     if n == 0: return 0 # base case 
     return (n % 10) + fun(n // 10)
n = 123456 
print(fun(n))