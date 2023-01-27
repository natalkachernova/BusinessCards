from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self,
                name: str,
                surname: str,
                phone_number: str,
                email: str
               ) -> None:
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
    
    def str(self) -> str:
        return f'{self.name} {self.surname} {self.email}'

    def length_name(self):
        return len(self.name + ' ' + self.surname)
  
    def contact(self):
        print("Connecting with ...")
        print(f' {self.name} \n {self.surname} \n {self.email} \n {self.company_name} \n {self.position}')
        print(f'I dial {self.phone_number} and call to {self.name} {self.surname}.')

class BusinessContact(BaseContact):
    def __init__(self, company_name, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_name = company_name
        self.position = position

base_contact_book = []

number_cards = int(input("Number of business cards: "))

for j in range(number_cards):    
    base_contact_book.append(BusinessContact(name = fake.first_name(), 
                                        surname = fake.last_name(), 
                                        phone_number = fake.phone_number(),
                                        email = fake.email(),
                                        company_name = fake.company(), 
                                        position = "Occupational social worker"))

for card in base_contact_book:   
    print(BaseContact.str(card))
print("--------- Sorted by name -------")
by_name = sorted(base_contact_book, key=lambda card: card.name)
for card in by_name:
    print(BaseContact.str(card))
print("--------- Sorted by surname ----")
by_surname = sorted(base_contact_book, key=lambda card: card.surname)
for card in by_surname:
    print(BaseContact.str(card))
print("--------- Sorted by email ------")
by_email = sorted(base_contact_book, key=lambda card: card.email)
for card in by_email:
    print(BaseContact.str(card))
print("--------- Send an email and call -------")
name_to_send = input("Enter the recipient's name: ")
for card in base_contact_book:
    if name_to_send == card.name:
        card.contact() 
        print("Legth Name and Surname: ", card.length_name())
        break