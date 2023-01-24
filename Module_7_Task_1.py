from faker import Faker
fake = Faker()

class ContactCard:
    def __init__(self,
                name: str,
                company_name: str,
                surname: str,
                position: str,
                email: str
               ) -> None:
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.email = email

    
    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.email}'


class BaseContact(ContactCard):
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def length_name(self):
        return len(self.name + ' ' + self.surname)
  
    def contact(self):
        print("Connecting with ...")
        print(f' {self.name} \n {self.surname} \n {self.email}')
        print(f'I dial {self.phone_number} and call to {self.name} {self.surname}.')


class BusinessContact(ContactCard):
    def __init__(self, company_name, position):
        self.company_name = company_name
        self.position = position

BaseContacts_Book = []
BusinessBaseContacts_Book = []

number_cards = int(input("Number of business cards: "))

for j in range(number_cards):
    
    BaseContacts_Book.append(BaseContact(name = fake.first_name(), 
                                        surname = fake.last_name(), 
                                        phone_number = fake.phone_number(),
                                        email = fake.email()))
    BusinessBaseContacts_Book.append(BusinessContact(company_name = fake.company(), 
                                                    position = "Occupational social worker"))

for i in range(number_cards):    
    print(ContactCard.__str__(BaseContacts_Book[i]))
print("--------- Sorted by name -------")
by_name = sorted(BaseContacts_Book, key=lambda Busines_Card: Busines_Card.name)
for i in range(number_cards):    
    print(ContactCard.__str__(by_name[i]))
print("--------- Sorted by surname ----")
by_surname = sorted(BaseContacts_Book, key=lambda Busines_Card: Busines_Card.surname)
for i in range(number_cards):    
    print(ContactCard.__str__(by_surname[i]))
print("--------- Sorted by email ------")
by_email = sorted(BaseContacts_Book, key=lambda Busines_Card: Busines_Card.email)
for i in range(number_cards):    
    print(ContactCard.__str__(by_email[i]))
print("--------- Send an email and call -------")
name_to_send = input("Enter the recipient's name: ")
for i in range(number_cards):
    if name_to_send == BaseContacts_Book[i].name:
        BaseContact.contact(BaseContacts_Book[i])
        print("Legth Name and Surname: ", BaseContact.length_name(BaseContacts_Book[i]))
        break