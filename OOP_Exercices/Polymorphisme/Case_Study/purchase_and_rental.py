from validinput import Validinput

class Purchase:
    def __init__(self,
                 price='',
                 taxes='',
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes



    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))


    @staticmethod
    def prompt_init():
        return dict(
            price = input("What is the seeling price? "),
            taxes = input("What are the estimated taxes? ")
        )




class Rental:
    def __init__(self,
                 furnished = '',
                 utilities = '',
                 rent ='',
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities



    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilites: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))



    @staticmethod
    def prompt_init():
        return dict(
            rent = input("What is the monthly rent? "),
            utilites = input("What are the estimated utilities? "),
            furnished = Validinput.get_valid_input("is the property furnished? ",
                                                   ("yes", "no"))
        )

