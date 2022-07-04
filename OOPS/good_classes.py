class Car:
    # constructor
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine

    def self_driving(self,engine):
        print("The car type is {} engine ".format(engine))


car1=Car(4,4,"petrol")
print("The no of tyres in object car1 is {}".format(car1.tyres))
print("The no of windows in object car1 is {}".format(car1.windows))
car1.self_driving("electric")


        