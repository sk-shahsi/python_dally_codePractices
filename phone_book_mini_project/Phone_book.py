class PhoneBook:
    phone_directory=[]
    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        PhoneBook.phone_directory.append(self)


    def show_contact(self):
        return f"Name:{self.name}, Contact number:{self.phone}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("NO contact found in the directory")
        else:
            for contact in cls.phone_directory:
                print(contact)

c1 = PhoneBook("jon",98745612387)
c2 = PhoneBook("jack",9956487859)
print(PhoneBook.phone_directory)
print(c1.show_contact())
print(c2.show_contact())

c1.show_all_contact()
c2.show_all_contact()

