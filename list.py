l=[1,2,3,4,5,6]
print(l)
print(type(l))

f=["apple","mango","chery"]
print(f)

mix=[1,"abc",5.5,True]
print(mix[2])
mix[2]=7.5
print(mix[2])
print(mix)

for i in mix:
    print(i)

for i in range(len(mix)):
    print(mix[i])

mix=[1,"abc",5.5,True]
print(mix[-2:-1])

print(mix[::-1])