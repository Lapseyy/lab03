# Edmarck Sosa, Due by 9/10/24, a Python program that performs as a Tuffy Titan Contact List which contains a list of contacts that can be modified or deleted.

import contacts

def menu():
    
    print("*** TUFFY TITAN CONTACT MAIN MENU")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit program")
    # choice = input(" Enter menu choice: ")   
 
def main():
    # contacts_list = [["Richard","Stallman"],["Bill","Gates"]]
    contacts_list = []
    while True:
        menu()
        choice = input("Enter menu choice: ")
        #print(choice.isdigit())
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                # print("1 Choice is selected.")
                contacts.print_list(contacts_list)
                
            elif choice == 2:
                # print("2 Choice is selected.")
                # fn = inut
                contact_list = contacts.add_contact(contacts_list, first_name = input("insert first name: "), last_name = input("insert last name: "))
                #contact_list = contacts.add_contact(contacts_list, firstName=input(), lastName=input())
                
            elif choice == 3:
                # print("3 Choice is selected.")
                #ccontact_list = contacts.modify_contact(contacts_list,userIndex= input("Index to update: "),  firstName=input("New first name: ",))
                ccontact_list = contacts.modify_contact(contacts_list, index= input("Index to update: "), first_name= "", last_name= "")
            
            elif choice == 4:
                # print("4 Choice is selected.")
                contact_list = contacts.delete_contact(contacts_list, index=input())
                
            elif choice == 5:
                # print("5 Choice is selected.")
                # sort by first name
                contact_list = contacts.sort_contacts(contacts_list, column=input()) 
                
            
            elif choice == 6:
                # print("6 Choice is selected.")
                # sort by last name
                contact_list = contacts.sort_contacts(contacts_list, column=input()) 
                
                
            elif choice == 7:
                # print("5 Choice is selected.")
                # print("Exiting program.")
                break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
            