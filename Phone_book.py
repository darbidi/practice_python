class Contact():
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
class Phonebook():
    def __init__(self):
        self.contacts=[]
    def add_contact(self,name,phone):
        new_person=Contact(name,phone)
        self.contacts.append(new_person)
    def search_contact(self,name):
        for person in self.contacts:
            if person.name == name :
                return person

        return None

