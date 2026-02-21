class MyString:
    def __init__(self, s):
        self.s = s

    def __mul__(self, n):
        return self.s * n

# Usage
s = input("Enter string: ")
n = int(input("Enter number of repetitions: "))
obj = MyString(s)
print(obj * n)
