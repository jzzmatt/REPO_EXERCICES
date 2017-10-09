class Property:
    def __init__(self,
                 square_feet='',
                 beds='',
                 baths='',
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths



    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    @staticmethod
    def prompt_init():
        '''This method use the Python dict constructor to create a dictionnary of values
            that can be passed into __init__, the value of each keys is prompted with a call to input
            '''
        return dict(square_feet= input("Enter the square feet: "),
                    beds= input("Enter number of bedrooms: "),
                    baths = input("Enter number of baths: ")
                    )
