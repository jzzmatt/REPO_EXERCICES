from house import House
from purchase_and_rental import Purchase, Rental




class HouseRental(Rental, House):

    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init




init = HouseRental.prompt_init()

house = HouseRental(**init)
#house.display()

#print(HouseRental.__mro__)

'''
TESTING


house = HouseRental()
house.display()
print(house.prompt_init())






#house = HouseRental(**init)
#house.d

'''
