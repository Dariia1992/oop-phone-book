class Contact:
    def __init__(self,id,name,email,phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        
    def show_info(self):
        print(f"id - {self.id} |first name - {self.name} |email - {self.email} |phone - {self.phone}")
        
