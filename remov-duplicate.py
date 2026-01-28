n = int(input("Enter number of elements: "))
nums = [int(input()) for _ in range(n)]
nums = list(set(nums))
print("List without duplicates:", nums)
