t = (('333', '33'), ('1416', '55'))
new_t = tuple(tuple(int(x) for x in pair) for pair in t)
print("Original:", t)
print("Converted:", new_t)
