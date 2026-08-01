class Animal:
    def sound(self):
        print("The animal makes a sound.", self.s)

    def eat(self):
        print("The animal eats ", self.food)
        
    def display(self):
        print("The name of the animal is:", self.name)
        print("The color of the animal is:", self.color)

dog=Animal()
dog.name="Dog"
dog.color="Brown"
dog.display()

dog.food="Dog Food"
dog.eat()


cat=Animal()
cat.name="Cat"
cat.color="White"
cat.display()

cat.s="Meow"
cat.sound()
