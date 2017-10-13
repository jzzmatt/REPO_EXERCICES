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

    def display(self):
        #return encrypted password , not plain text
       user_list = [(account.username,account.password) for account in Account.account_list]
       return user_list


class PasswordValidation(Account):

    def __init__(self,username, password):
        super().__init__(username, password)


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

    def total_Scan(self):
        if self.check_length() and self.check_Number() and self.check_espcial_char():
            return ("Account {}, password Total Scan Complete".format(self.username))
        return False




#junior = Account("junior", "Checkk2009$")
junior = PasswordValidation("Junior", "Checkk2009")
#print(PasswordValidation(junior.password).check_length())
#print(PasswordValidation(junior.password).check_espcial_char())
#print(PasswordValidation(junior.password).check_Number())
print(junior.display())
#print(junior.total_Scan())




