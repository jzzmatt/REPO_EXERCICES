from contactList import ContactList  #we Import ContactList that hold code for built_in class

class Contact:
    'this class will Hold all contact object or instance'
    all_contact = ContactList()


    def __init__(self, name, email):
        self.name = name
        self.email = email
        #Contact.all_contact.append(self)  #this list will old all Obj or instance => self
        self.all_contact.append(self)



class Supplier(Contact):
    def order(self, order):
        return ("If this were a real system we would send {} order to {}".format(order, self.name))



class MailSender:
    def send_mail(self, message):
        print("Sending mail to {}".format(self.email))
        #Adding email logic


class EmailableContact(Contact, MailSender):
    pass



'''
Let's  Test the inheritance from Supplier , that extend Contact

TEST 1
c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email, s.name, s.email)
print(c.all_contact)
print(s.all_contact)

#print(c.order("Inneed pliers")) #this will return an error, as Contact not contain a order method
print(s.order("Inned pliers"))

TEST 2
c1 = Contact("John a", "johna@example.net")
c2 = Contact("John b", "johnb@example.net")
c3 = Contact("Jenna c", "jenna@example.net")

print([c.name for c in Contact.all_contact.search('John')])




#TEST 3 email test

e = EmailableContact("John Smith", "jsmith@example.net")

print(Contact.all_contact)

e.send_mail("Hello , test email smtp")

'''

