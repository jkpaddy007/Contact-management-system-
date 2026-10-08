FILE_NAME = "contacts.txt"

def load_contacts():
contacts = {}

try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.rstrip("\n").split("|")

            if len(parts) == 3:
                name, phone, email = parts
                contacts[phone] = {
                    "name": name,
                    "email": email
                }

except FileNotFoundError:
    pass

return contacts

def save_contacts(contacts):
with open(FILE_NAME, "w") as file:
for phone, details in contacts.items():
file.write(
f"{details['name']}|{phone}|{details['email']}\n"
)

def add_contact(contacts):
name = input("Enter name: ").strip()
phone = input("Enter phone number: ").strip()
email = input("Enter email: ").strip()

if not name or not phone:
    print("Name and phone number are required.")
    return

if "|" in name or "|" in phone or "|" in email:
    print("The | character is not allowed.")
    return

if phone in contacts:
    print("This phone number already exists.")
    return

contacts[phone] = {
    "name": name,
    "email": email
}

save_contacts(contacts)
print("Contact added successfully!")

def view_contacts(contacts):
if not contacts:
print("No contacts found.")
return

for phone, details in contacts.items():
    print(f"Name: {details['name']}")
    print(f"Phone: {phone}")
    print(f"Email: {details['email']}")
    print("-" * 30)

def search_contact(contacts):
search = input("Enter name or phone number: ").strip().lower()

found = False

for phone, details in contacts.items():
    if (
        search in details["name"].lower()
        or search in phone.lower()
    ):
        print(f"Name: {details['name']}")
        print(f"Phone: {phone}")
        print(f"Email: {details['email']}")
        found = True

if not found:
    print("Contact not found.")

def update_contact(contacts):
phone = input("Enter phone number of contact to update: ").strip()

if phone not in contacts:
    print("Contact not found.")
    return

name = input("Enter new name: ").strip()
email = input("Enter new email: ").strip()

if not name:
    print("Name cannot be empty.")
    return

if "|" in name or "|" in email:
    print("The | character is not allowed.")
    return

contacts[phone] = {
    "name": name,
    "email": email
}

save_contacts(contacts)
print("Contact updated successfully!")

def delete_contact(contacts):
phone = input("Enter phone number to delete: ").strip()

if phone in contacts:
    del contacts[phone]
    save_contacts(contacts)
    print("Contact deleted successfully!")
else:
    print("Contact not found.")

def main():
contacts = load_contacts()

while True:
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

if name == "main":
main()
