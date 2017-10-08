'''
<---- EXTENDED BUILT_IN CLASS ------>
One of the goal of extend Built-in class, is to add funcionality to built-in class
Instead of instantiating a normal list as our class variable, we create a new ContactList
class that extends the built-in list
Then we instantiate this subclass as our all_contact list
'''

class ContactList(list):

    def search(self, name):
        '''
        :param name:
        :return: Return all Contact Obj or instance that contains the search value in their name
        '''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


