lst = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Sorted list:", lst)
