a=input("Enter a value: ")
if a.isdigit():
    print("The input is an integer.")
elif a.replace('.','',1).isdigit() and a.count('.') < 2:
    print("The input is a float.") 
elif a.isalpha():
    print("The input is a string.")
elif a.lower() in ['true', 'false']:
    print("The input is a boolean.")
else:
    print("The input is of an unknown type.")