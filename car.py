class Car:
    wheels="4 wheeler"
    
    def __init__(self,B_name,color):
        self.B_name=B_name
        self.color=color

    def display(self):
        print("Brand Name :",self.B_name)
        print("Color :",self.color)
        print("Wheels in Car : ",self.wheels)

car1=Car("BMW","Black")
car1.display()

car2=Car("RR","Grey")
car2.wheels="2 wheeler"
car2.display()