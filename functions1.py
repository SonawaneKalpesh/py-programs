def evenOdd(n):
    if n % 2 == 0:
        return (n, "number is Even")
    return (n, "number is Odd")


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def primeOrNot(n):
    if n <= 1:
        return (n, "is not prime")
    for i in range(2, n):
        if n % i == 0:
            return (n, "is not prime")
    return (n, "is prime")


def countDigit(n_str):
    return len(n_str)


def sumDigit(n_str):
    return sum(int(ch) for ch in n_str)


def ReverseNo(n_str):
    return n_str[::-1]


def callFunction(a):
    
    if a < 0:
        print("Please enter a positive number.")
        return

    a_str = str(a)

    print(evenOdd(a))
    print("factorial:", factorial(a))
    print(primeOrNot(a))
    print("countDigit:", countDigit(a_str))
    print("sumDigit:", sumDigit(a_str))
    print("ReverseNo:", ReverseNo(a_str))


a = int(input("enter a number : "))
callFunction(a)


