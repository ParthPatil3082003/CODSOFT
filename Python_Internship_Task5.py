import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Manager By Parth Patil")

        # Create and place widgets
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone = tk.Label(root, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(root)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_address = tk.Label(root, text="Address:")
        self.label_address.grid(row=3, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(root)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        self.button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_view_all = tk.Button(root, text="View All Contacts", command=self.view_all_contacts)
        self.button_view_all.grid(row=5, column=0, columnspan=2, pady=10)

        self.label_search = tk.Label(root, text="Search:")
        self.label_search.grid(row=6, column=0, padx=10, pady=5)
        self.entry_search = tk.Entry(root)
        self.entry_search.grid(row=6, column=1, padx=10, pady=5)

        self.button_search = tk.Button(root, text="Search", command=self.search_contact)
        self.button_search.grid(row=7, column=0, columnspan=2, pady=10)

        self.button_exit = tk.Button(root, text="Exit", command=root.destroy)
        self.button_exit.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entry_fields()
        else:
            messagebox.showerror("Error", "Name and phone are required!")

    def clear_entry_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

    def view_all_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts to display.")
        else:
            contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        query = self.entry_search.get().lower()
        if query:
            matching_contacts = [contact for contact in self.contacts if query in contact.name.lower() or query in contact.phone]
            if matching_contacts:
                contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in matching_contacts])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search query.")

# Create the main window
root = tk.Tk()
app = ContactManagerApp(root)
root.mainloop()
