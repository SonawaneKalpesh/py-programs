f=["apple","mango","cherry"]
f.append("banana")
f.extend(["grapes","kiwi"])
f.insert(2,"orange")
f.remove("mango")
f.pop(3)


print(f.index("kiwi"))
f.reverse()
print(f)
f.clear()