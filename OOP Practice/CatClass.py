class Cat: #The classs naming convention is CapitalizedWords notation. e.g: MunchkinCat
    #pass  #used for empty class
    
    #Class attribute: define properties that should have the same value for every class instance.
    species = "Prionailurus bengalensis"
    
    #Instance attributes: for properties that vary from one instance to another.
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Creating a new object from a class is called instantiating an object
shiro = Cat("Shiro", 3)
kuro = Cat("Kuro", 5)

#You can also chenge the attribute values
shiro.age = 5 

kuro.species = "Felis chaus"

print(shiro.name, shiro.age, shiro.species)
print(kuro.name, kuro.age, kuro.species)
