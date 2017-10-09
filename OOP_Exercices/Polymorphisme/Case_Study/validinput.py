class Validinput(object):

    @staticmethod
    def get_valid_input(input_string, valid_options):

        input_string += "({})".format(" ,".join(valid_options))
        response = input(input_string)

        while response.lower() not in valid_options:
            response = input(input_string)  #Actualy just update the response but with no roles

        return(response)  #else response is in the tuples, return this elemn in tuples


'''

#TESTING
print(Validinput.get_valid_input("What laundry? ", ("coin", "ensuite", "none")))
'''