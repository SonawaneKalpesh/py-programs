try:
    n = int(input("Enter a positive integer: "))
    if n > 0:
        print("Correct input:", n)
    else:
        print("Error: Number is not positive!")
except ValueError:
    print("Error: Invalid input! Please enter an integer.")
