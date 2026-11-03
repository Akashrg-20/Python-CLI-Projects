from contact import Contact
from database import cursor,conn
import sqlite3


def validate_phone(number):
    return len(number)==10 and number.isdigit()


def add_contact(contact:Contact):

    valid_phone=validate_phone(contact.phone)

    if not valid_phone:
        print("\nInvalid phone number\n")
        return

    
    try:
        query="INSERT INTO CONTACTS (NAME,PHONE) VALUES (?,?)"
        cursor.execute(query, (contact.name, contact.phone))
        conn.commit()
        print("\nContact added successfully!\n")

    except sqlite3.IntegrityError:
        print("\nPhone number already exists!\n")


def view_all_contacts():
    query="SELECT * FROM CONTACTS"

    cursor.execute(query)
    contacts=cursor.fetchall()

    if not contacts:
        print("\nNo contacts found")
        return

    print("\nContacts: ")
    for contact in contacts:
        print(contact)

    print("\n")

def search_contact(key,value):
    # key = column name
    # value = name or phone

    if key=="NAME":
        value=value.strip().lower()
    
    query=f"SELECT * FROM CONTACTS WHERE {key}=?"

    cursor.execute(query,(value,))
    contacts=cursor.fetchall()


    if not contacts:
        print(f"\nNo contact found by {value}\n")
        return
    
    print("\nContacts: ")
    for contact in contacts:
        print(contact)
    
    print("\n")


def update_contact(id,key,new_value):
    query="SELECT * FROM CONTACTS WHERE ID=?"
    data=cursor.execute(query,(id,)).fetchone()

    if key=="NAME":
        new_value=new_value.strip().lower()
    
    if not data:
        print("Contact not found")
    else:
        query=f"UPDATE CONTACTS SET {key}=? WHERE ID=?"
        cursor.execute(query,(new_value,id))
        conn.commit()

        print("\nUpdated successfully\n")

    


def delete_contact(id):
    query="DELETE FROM CONTACTS WHERE ID=?"
    cursor.execute(query,(id,))
    conn.commit()

    if cursor.rowcount==0:
        print("\nContact not found\n")
    else:
        print("\nContact deleted successfully\n")
               


def delete_all_contacts():
    query="DELETE FROM CONTACTS"
    cursor.execute(query)
    conn.commit()

    print("\nContacts deleted successfully..\n")

        

def main():
    while True:
        print("================================")
        print("CONTACT BOOK APP")
        print("================================")

        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Delete all contacts")
        print("7. Exit")

        print("================================")

        try:
            user_choice=int(input("Enter your choice: "))

            match user_choice:
                case 1:
                    name = input("Enter name: ")
                    phone = input("Enter phone number: ")

                    con = Contact(name, phone)
                    add_contact(con)

                case 2:
                    view_all_contacts()

                case 3:
                    print("Select : ")
                    print("1.Search by Name")
                    print("2.Search by phone number\n")

                    choice=int(input("Enter your input: "))
                    if choice==1:
                        value=input("Enter name: ")
                        search_contact("NAME",value)
                    elif choice==2:
                        value=input("Enter phone number: ")
                        search_contact("PHONE",value)
                    else:
                        print("INVALID INPUT, TRY AGAIN NEXT TIME...")
                        break

                case 4:
                    print("Select : ")
                    print("1.Update Name")
                    print("2.Update phone number")
                    
                    choice=int(input("Enter your input: "))
                    if choice==1:
                        view_all_contacts()

                        id=input("\nEnter id: ")
                        new_name=input("Enter name (new): ")
                        update_contact(id,"NAME",new_name)

                    elif choice==2:
                        view_all_contacts()

                        id=input("\nEnter id: ")
                        new_phone=input("Enter phone number (new): ")
                        
                        valid_phone=validate_phone(new_phone)
                        
                        if valid_phone:
                            update_contact(id,"PHONE",new_phone)
                        else:    
                            print("Invalid phone number")
                        
                        
                    else:
                        print("INVALID INPUT, TRY AGAIN NEXT TIME...")
                        
                                       

                case 5:
                    view_all_contacts()

                    id=input("Enter id: ")
                    delete_contact(id)
                    

                case 6:
                    confirm = input("Are you sure? (yes/no): ").strip().lower()

                    if confirm=="yes": 
                        delete_all_contacts() 
                    else: 
                        print("Operation cancelled")

                    

                case 7:
                    print("Thank you for using Contact Book!")
                    conn.close()
                    break

                case _:
                    print("Invalid choice. Try again.")

        except ValueError:
            print("INVALID INPUT, TRY AGAIN NEXT TIME...")
        


if __name__=="__main__":
    main()
