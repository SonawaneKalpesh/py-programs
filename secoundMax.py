lst=[11,18,5,6,7,8,9,10]
max1=lst[0]
max2=0
for i in lst:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2 and i!=max1:
        max2=i
print("Second maximum number is:",max2)