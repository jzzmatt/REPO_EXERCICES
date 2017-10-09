from property import Property
from validinput import Validinput


#def get_valid_input(input_string, valid_options):
#    input_string += "({})".format(" ,".join(valid_options))
#    response = input(input_string)

#    while response.lower() not in valid_options:
#        response = input(input_string)
#    return response



class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")


    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry



    def display(self):
        super().display()
        print("APARTMENT DETAILS")  #add this statement after super().display
        print("laundry: {}".format(self.laundry))
        print("has balcony {}".format(self.balcony))


    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init() #Call this static method from SuperClass

        #laundry = ''

        #while laundry.lower() not in Apartment.valid_laundries:
        #    laundry = input("What laundry facilities does the property have? ({})".format(
         #       ", ".join(Apartment.valid_laundries)))


         #   balcony = ''
         #   while balcony.lower() not in Apartment.valid_balconies:
         #       balcony =input("Does the property have a balcony? ({})".format(
         #         ", ".join(Apartment.valid_balconies)))
        laundry = Validinput.get_valid_input("What laundry facilites does the property have? ", Apartment.valid_laundries)

        balcony = Validinput.get_valid_input("Does the property have balcony? ", Apartment.valid_balconies)

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })

        return parent_init


'''
TESTING & CHECK INHERITANCE

print(Apartment.__mro__)


apt = Apartment.prompt_init()

print(apt)
'''


