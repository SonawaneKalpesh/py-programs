def calculate(*numbers, operation="sum"):
    if operation == "sum":
        print(sum(numbers))
    elif operation == "max":
        print(max(numbers))
    elif operation == "min":
        print(min(numbers))
    elif operation == "sorted":
        print(sorted(numbers))
    else:
        print("Invalid operation")


calculate(10, 20, 30)
calculate(10, 20, 30, operation="max")
calculate(10, 20, 30, operation="min")
calculate(10, 20,5, 30, operation="sorted")