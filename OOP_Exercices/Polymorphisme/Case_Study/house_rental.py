from house import House
from purchase_and_rental import Rental




class HouseRental(Rental, House):


    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init




h = HouseRental()

print(h.prompt_init())
'''
TESTING


house = HouseRental()
house.display()




#init = HouseRental.prompt_init()

#house = HouseRental(**init)
#house.display()

#house = HouseRental(**init)
#house.d

'''
