from services.phone_book import PhoneBook


book = PhoneBook()
book.load_contacts()


choice = True

while choice:
    print("\n===== PHONE BOOK =====")
    print("1. Show all contacts")
    print("2. Find contact")
    print("3. Add contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("0. Exit")
    print("======================")

    choice = input("Enter your choice: ").strip()

    if not choice.isdigit():
        print("Please enter a number")
        continue

    choice = int(choice)

    # SHOW ALL CONTACTS
    if choice == 1:
        book.show_contacts()

    # FIND CONTACT
    elif choice == 2:
        print("\n===== FIND CONTACT =====")
        print("1. Find by name")
        print("2. Find by ID")
        print("3. Find by phone")
        print("========================")

        search_choice = input("Choose search type: ").strip()

        if search_choice == "1":
            name = input("Enter name: ").strip()
            contact = book.find_contact(name)

        elif search_choice == "2":
            contact_id = input("Enter ID: ").strip()

            if not contact_id.isdigit():
                print("Incorrect ID")
                continue

            contact_id = int(contact_id)
            contact = book.find_id(contact_id)

        elif search_choice == "3":
            phone = input("Enter phone: ").strip()
            contact = book.find_phone(phone)

        else:
            print("Incorrect choice")
            continue

        if contact:
            contact.show_info()
        else:
            print("Contact not found")

    # ADD CONTACT
    elif choice == 3:
        name = input("Enter name: ").strip()

        if not name.isalpha():
            print("Incorrect name")
            continue

        email = input("Enter email: ").strip()

        if "@" not in email or "." not in email:
            print("Incorrect email")
            continue

        phone = input("Enter phone: ").strip()

        if not phone.isdigit():
            print("Enter numbers only!")
            continue

        new_contact = book.add_contact(name, email, phone)
        book.save_contacts()
        print("Contact added ✅")
        new_contact.show_info()

    # UPDATE CONTACT
    elif choice == 4:
        name = input("Enter name: ").strip()

        if not name.isalpha():
            print("Incorrect name")
            continue

        new_email = input("Enter new email: ").strip()

        if "@" not in new_email or "." not in new_email:
            print("Incorrect new email")
            continue

        new_phone = input("Enter new phone: ").strip()

        if not new_phone.isdigit():
            print("Enter numbers only!")
            continue

        updated = book.update_contact(
            name,
            new_email,
            new_phone
        )

        if updated:
            book.save_contacts()
            print("Contact updated")
        else:
            print("Contact not found")

    # DELETE CONTACT
    elif choice == 5:
        name = input("Enter name: ").strip()

        deleted = book.delete_contact(name)

        if deleted:
            book.save_contacts()
            print("Contact deleted")
        else:
            print("Contact not found")

    # EXIT
    elif choice == 0:
        choice = False
        print("Goodbye!")

    else:
        print("Incorrect choice")