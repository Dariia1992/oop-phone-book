from models.contact import Contact
import csv



class PhoneBook():
    def __init__(self):
        self.contacts = []
        
    def load_contacts(self):
        with open("contact.csv", "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                contact = Contact(
                int(row["id"]),
                row["first_name"],
                row["email"],
                row["phone"]
            )
                self.contacts.append(contact)
                
    def save_contacts(self):
        with open("contact.csv", "w", encoding="utf-8", newline="") as f:
            fieldnames = ["id", "first_name", "email", "phone"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({
                "id": contact.id,
                "first_name": contact.name,
                "email": contact.email,
                "phone": contact.phone
            })
        
    def add_contact(self, name, email, phone):
        max_id = max(int(contact.id) for contact in self.contacts)
        new_id = max_id + 1

        contact = Contact(new_id, name, email, phone)
        self.contacts.append(contact)
        
        return contact
    
    def show_contacts(self):
        for people in self.contacts:
            people.show_info()
            
    def find_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None
    
    def find_id(self, contact_id):
        for contact in self.contacts:
            if contact.id == contact_id:
                return contact

        return None
    
    def find_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
               return contact

        return None
       
    
    def update_contact(self,name, new_email, new_phone):
        contact = self.find_contact(name)
        if contact:
            contact.email = new_email
            contact.phone = new_phone
            return True
        return False
                
            
    def delete_contact(self,name):
        contact = self.find_contact(name)
        
        if contact in self.contacts:
            self.contacts.remove(contact)
            return True

        return False
        
#python -m services.phone_book (zapusk file)