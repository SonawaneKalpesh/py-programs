t = (1, 2, 3, 2, 4, 1, 5, 3, 3)
rep = []
for i in t:
    if t.count(i) > 1 and i not in rep:
        rep.append(i)
print("Repeated items:", rep)
