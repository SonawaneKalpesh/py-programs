d = {'a':1, 'b':2, 'c':3}
k = input("Enter key: ")
if k in d:
    nk = input("New key: ")
    nv = input("New value: ")
    d.pop(k)
    d[nk] = nv
else:
    print("Key not found!")
print("Updated dict:", d)
