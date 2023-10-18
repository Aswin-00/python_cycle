'''

Sample Output:

Contact Application Menu:
1. Add Contact
2. Update Contact
3. Delete Contact
4. List Contacts
5. Quit
Enter your choice: 1

Enter the name: Alice
Enter the phone number: 123-456-7890
Enter the email: alice@example.com

Contact Application Menu:
1. Add Contact
2. Update Contact
3. Delete Contact
4. List Contacts
5. Quit
Enter your choice: 4

Contacts:
Name: Alice, Phone Number: 123-456-7890, Email: alice@example.com
Name: Bob, Phone Number: 987-654-3210, Email: bob@example.com


'''
from contact import contact

def main():
    sample=contact()
    print('''
Contact Application Menu:
1. Add Contact
2. Update Contact
3. Delete Contact
4. List Contacts
5. Quit
    ''')
    choice=int(input('Enter your choice: '))

    if choice ==1:
        name=input('Enter the name: ')
        ph_num=input('Enter the phone number: ')
        email=input('Enter the email: ')

        sample.add_contact(name,ph_num,email)
        sample.list_contacts()
    elif choice==2:
        name=input('Enter the Contact name: ')
        ph_num=input('Enter the New  phone number: ')
        email=input('Enter the New  email: ')
        
        sample.update_contact(name,ph_num,email)



if __name__=="__main__":
    main()
