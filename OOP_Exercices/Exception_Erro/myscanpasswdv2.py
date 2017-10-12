'''
PASSWORD STORAGE
Create an Account (Username, Password)
ForgetPassword, Enter 3 Answer to 3 Question for Password Recovery
Encrypted the plain text password and Store it
Search an Account
Recovery an Account password 
Deencrypted password

'''
import re

class Account(object):
    account_list = []

    def __init__(self, username, password):
            self.username = username
            self.password = password

            Account.account_list.append(self)



class PasswordValidation():

    def __init__(self, password):
        self.password = password
        self.valid = []


    def check_length(self):
        return len(self.password) >= 6


    def check_Number(self):
        if re.search('[0-9]', self.password) != None:
            return True
        return False


    def check_espcial_char(self):
            if re.search('[$#@]', self.password) != None:
                return True
            return False




junior = Account("junior", "Checkk2009$")
#print(PasswordValidation(junior.password).check_length())
#print(PasswordValidation(junior.password).check_espcial_char())
#print(PasswordValidation(junior.password).check_Number())



