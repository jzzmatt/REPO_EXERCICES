class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **kwargs):  # Any other Arg , will be accepted
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        '''

        :param street: 
        :param city: 
        :param state: 
        :param code: 
        :param kwargs: If we have an arg , that are note handled by manual attribute,
        forwad it to the superclass 
        '''
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        '''

        :param phone: 
        :param kwargs: Here, when, we will initialize  or instantiate  this Class
        only phone attribute which is explicitly define  will be  visible, 
        any other arg as **kwarg have to be define by the user, & then will be handled by the superclass
        Now
        Which superclass will handled the unknow arg , 
        check the class.__mro__ to check the Order
        '''
        print(kwargs)
        super().__init__(**kwargs)
        self.phone = phone


f1 = Friend(923033029, name='junior', email='jmateus@gmail.com', state='Angola', city='Luanda')
f2 = Friend(923033000, name='mateus', email='mateus@gmail.com', state='US', city='Boston')

print("here is the mro or the lookup for get **kwargs :\n{}".format(Friend.__mro__))
print([contact.name for contact in f1.all_contacts])
print([contact.city for contact in f1.all_contacts])