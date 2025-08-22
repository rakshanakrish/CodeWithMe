# We use getter and setter function to access a private variable
class car:
    def __init__(self,car_name,seat,mileage):
        self.car_name=car_name
        self.seat=seat
        self.__mileage=mileage #if __ is added then it is private variable
    def __del__(self):
        print("This is a Destructor of",self)

    '''just self gives u a location name or id(self) gives u a memory location of each object 
To specify what it should print in term of self is printed we use "__str__" '''

    def __str__(self): 
        return self.car_name
    def forward(self,speed):
        print("Car moving forward",speed)
    def backward(self,speed):
        print("Car moving backward",speed)
    def get_mileage(self):
        return self.__mileage
    def set_mileage(self,mileage):
        self.__mileage=mileage
car1=car('Audi',4,20)
car2=car('BMW',4,24)
car3=car('Ertiga',7,19)
car1.set_mileage(25)
print(car1.get_mileage())
print(car2.car_name,car2.seat,car2.get_mileage())
print(car3.car_name,car3.seat,car3.get_mileage())

