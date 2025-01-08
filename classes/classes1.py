# Here the goal is to learn about classes in python
 # So a class is  the blueprint for creating objects it contains attributes and properties of an objects]


# creatiing a class for a cat
class Cat:
    # the _innit_  is the constructor of the class
    def __init__(self, name, age, color):
        # the name, age, color are the attributes.
        self.name = name
        self.age = age
        self.color = color
    
    #Methods here are the things that the  object can  do (here we are refering to the cat)
    # Lets use the meow as a method

    def meow(self) :
        print(self.name, 'says Meow')
        print(self.name, 'age is ', self.age)
        print(self.name, 'color is ', self.color)
    
    def walking(self):
        print(self.name, 'is walking')
        

# here let us create a dog?

cat1 = Cat('Tom', 2, 'Black')
cat2 = Cat('Gary', 5, 'Grey')

#Lets call theh method meow fo rhe cats
cat1.meow()
cat2.meow()

cat1.walking()
cat2.walking()


# LEts try and save this in  a file

fileName = open('cats.txt', "w")

# write  the  cats details inside
# Create the lines using f-strings
line1 = f"We have two cats, their names are {cat1.name} and {cat2.name}.\n"
line2 = f"They are {cat1.age} and {cat2.age} years old respectively.\n"
line3 = f"They also have the colors {cat1.color} and {cat2.color}.\n"

fileName.write(line1)
fileName.write(line2)
fileName.write(line3)

# line4 = f"The cats, {cat1.walkin} and {cat2.walking} are walking along the lawn."
# fileName.write(line4)


fileName.close()