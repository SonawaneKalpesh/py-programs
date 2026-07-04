name=input("enter str")

upper=0
lower=0
for ch in name :
    if ch.isupper():
        upper+=1
    else :
        lower+=1

print("count of upper case charecters :",upper)
print("count of lower case charecters :",lower)