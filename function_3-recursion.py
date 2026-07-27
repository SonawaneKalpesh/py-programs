def fibo(a,b,n):
    if n==0:
        return 
    print(a,end=" ")
    fibo(b,a+b,n-1)


def sumNatureal(n):
    if n==0:
        return 0
    return  sumNatureal(n-1)+n

def reverse(n):
    if n<10:
        print(n,end=" ")
        return
    else:
        print(n%10,end=" ")
        reverse(n//10)

def sumDigit(n):
    if n==0:
        return 0
    return sumDigit(n//10)+n%10

def callAllfun(n):

    print("Fibonacci series is: ", end=" ")
    fibo(0,1,n)

    sum=sumNatureal(n)
    print("\nSum of natural numbers is:", sum)

    print("\nReverse of the number is: ", end=" ")
    reverse(n)

    sum=sumDigit(n)
    print("\nSum of digits of the number is:", sum)



n=int(input("Enter the number of terms: "))

callAllfun(n)