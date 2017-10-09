
from purchase_and_rental import Rental
from house import House



class HouseRental(Rental, House):


    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init







'''
TESTING
'''

#init = HouseRental.prompt_init()

#house = HouseRental(**init)
#house.display()

#house = HouseRental(**init)
#house.d
