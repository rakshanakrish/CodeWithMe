class car:
    def __init__(self,carname,mileage):
        self.carname=carname
        self.__mileage=mileage
    @property
    def mileage(self):
        return self.__mileage
    @mileage.setter
    def mileage(self,v):
        self.__mileage=v
car1=car('Inova',25)
print(car1.mileage)
car1.mileage=20
print(car1.mileage)