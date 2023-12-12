'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
22) Create a Python program that represents a contact application using a dictionary 
      to store contact information. The application should take user input and have the   
      following functionality:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Initialize an empty dictionary to store contact information.

2. Create functions or methods for the following operations:
   - `add_contact(name, phone_number, email)` - Add a new contact with the given name,  
      phone number, and email to the dictionary.
   - `update_contact(name, new_phone_number, new_email)` - Update the phone number 
       and email of an existing contact with the given name.
   - `delete_contact(name)` - Delete a contact with the given name.
   - `list_contacts()` - Display a list of all contacts in the dictionary.

Contacts:
Name: Alice, Phone Number: 123-456-7890, Email: alice@example.com
Name: Bob, Phone Number: 987-654-3210, Email: bob@example.com


'''


# create a class contact
class contact:
#Initialize an empty dictionary to store contact information.

    def __init__(self):
        self.contact_list={}

#-`add_contact(name, phone_number, email)`  

    def add_contact(self,name,phone_number,email):
        self.contact_list[name]={'Name':name,
                           'phone_number':phone_number,
                           'email':email
                           }
# -`update_contact(name, new_phone_number, new_email)` - Update the phone number 

    def update_contact(self,name,new_phone_number='',new_email=''):
        if new_phone_number =='' and new_email=='':
            print('no value given')
 
        else:
            self.contact_list[name]['phone_number']=new_phone_number
            self.contact_list[name]['email']=new_email
            


            
# - `delete_contact(name)` - Delete a contact with the given name.

    def delete_contact(self,name):
        self.contact_list.pop(name)
        



#  - `list_contacts()` - Display a list of all contacts in the dictionary.

    def list_contacts(self):
        for i in self.contact_list:
            print(f"Name: {self.contact_list[i]['Name']}, Phone Number: {self.contact_list[i]['phone_number']}, Email: {self.contact_list[i]['email']}")


if __name__=="__main__":
    c=contact()
    c.add_contact('aswin','9909185611','aswingirish00@gmail.com')
    c.add_contact('jithin','9959185611','aswingirish00@gmail.com')
##    c.list_contacts()    
    c.update_contact('aswin','768666667','bootpq@gmail.com')
##    c.list_contacts()
##    c.delete_contact('aswin')

    c.list_contacts()
