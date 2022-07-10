class Animal:
    def __init__(self,*args):
        if len(args)==1:
            self.name = args[0]
        elif len(args)==2:
            self.name = args[0]
            self.species = args[1]
        elif len(args)==3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    def make_sound(self, sound):
        return "The animal is {} and says {}".format(self.name, sound)

dog=Animal("dog","mammals",17)
print(dog.name)
print(dog.species)
print(dog.age)
print(dog.make_sound("woof wwoof"))