'''
PASSWORD STORAGE
Create an Account (Username, Password)
ForgetPassword, Enter 3 Answer to 3 Question for Password Recovery
Encrypted the plain text password and Store it
Recovery an Account password 


'''
import re
import hashlib

class Account(object):
    account_list = []

    def __init__(self, username, password):
            self.username = username
            if PasswordValidation(password).pass_all_scan():
                self.password = HashPassword(password).get_hash
            else:
                raise ValueError("Your Password doesn't meet complexity Requirement")



            Account.account_list.append(self)

    def display(self):
        #return encrypted password , not plain text
       user_list = [(account.username,account.password) for account in Account.account_list]
       return user_list





class PasswordValidation():

    def __init__(self, password):
        self._password = password

    def check_length(self):
        return len(self._password) >= 6


    def check_Number(self):
        if re.search('[0-9]', self._password) != None:
            return True
        return False


    def check_espcial_char(self):
            if re.search('[$#@]', self._password) != None:
                return True
            return False

    def pass_all_scan(self):
        if self.check_length() and self.check_Number() and self.check_espcial_char():
            return True
        return False


class HashPassword():
    def __init__(self, password):
        self._password = password

    @property
    def get_hash(self):
        _hashing_passwd = hashlib.sha1(str.encode(self._password)).hexdigest()
        return _hashing_passwd



osvald = Account("Osvald", "password20$$")
print(osvald.display())

#junior = Account("junior", "Checkk2009$")
#junior = PasswordValidation("Junior", "Checkk2009")
#print(PasswordValidation(junior.password).check_length())
#print(PasswordValidation(junior.password).check_espcial_char())
#print(PasswordValidation(junior.password).check_Number())
#print(junior.display())
#print(junior.total_Scan())




