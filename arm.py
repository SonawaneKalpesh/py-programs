def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == number

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        if is_armstrong(n):
            print(f"{n} is an Armstrong number.")
        else:
            print(f"{n} is not an Armstrong number.")
    except ValueError:
        print("Please enter a valid integer.")