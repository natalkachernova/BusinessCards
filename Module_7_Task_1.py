from faker import Faker
fake = Faker()

class Base_Contact:
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
        string1 = f" {self.name}\n {self.surname}\n {self.email}\n {self.company_name}\n {self.position}\n"
        string2 = f"I dial {self.phone_number} and call to {self.name} {self.surname}."
        return string1 + string2

class Business_Contact(Base_Contact):
    def __init__(self, company_name, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_name = company_name
        self.position = position

base_contact_book = []

number_cards = int(input("Number of business cards: "))

for j in range(number_cards):    
    base_contact_book.append(Business_Contact(name = fake.first_name(), 
                                        surname = fake.last_name(), 
                                        phone_number = fake.phone_number(),
                                        email = fake.email(),
                                        company_name = fake.company(), 
                                        position = "Occupational social worker"))

for i in range(number_cards):    
    print(Base_Contact.str(base_contact_book[i]))
print("--------- Sorted by name -------")
by_name = sorted(base_contact_book, key=lambda Busines_Card: Busines_Card.name)
for i in range(number_cards):    
    print(Base_Contact.str(by_name[i]))
print("--------- Sorted by surname ----")
by_surname = sorted(base_contact_book, key=lambda Busines_Card: Busines_Card.surname)
for i in range(number_cards):    
    print(Base_Contact.str(by_surname[i]))
print("--------- Sorted by email ------")
by_email = sorted(base_contact_book, key=lambda Busines_Card: Busines_Card.email)
for i in range(number_cards):    
    print(Base_Contact.str(by_email[i]))
print("--------- Send an email and call -------")
name_to_send = input("Enter the recipient's name: ")
for i in range(number_cards):
    if name_to_send == base_contact_book[i].name:
        print("Connecting with ...")
        print(Base_Contact.contact(base_contact_book[i]))
        print("Legth Name and Surname: ", Base_Contact.length_name(base_contact_book[i]))
        break