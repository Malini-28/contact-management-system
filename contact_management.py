# Contact Management System using Python (File Handling)

FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("✅ Contact added successfully!\n")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.\n")
            else:
                print("\n--- Contact List ---")
                for contact in contacts:
                    name, phone, email = contact.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")
                print()
    except FileNotFoundError:
        print("No contacts file found.\n")


def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"Found: {name}, {phone}, {email}\n")
                    found = True
                    break
        if not found:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts file found.\n")


def delete_contact():
    delete_name = input("Enter name to delete: ")
    contacts = []
    deleted = False

    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        with open(FILE_NAME, "w") as file:
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                if name.lower() != delete_name.lower():
                    file.write(contact)
                else:
                    deleted = True

        if deleted:
            print("✅ Contact deleted successfully!\n")
        else:
            print("Contact not found.\n")

    except FileNotFoundError:
        print("No contacts file found.\n")


def main():
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
