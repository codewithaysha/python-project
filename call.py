import tkinter as tk
from tkinter import messagebox

contacts = {}

# Functions
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()

    if name and phone:
        contacts[name] = phone
        messagebox.showinfo("Success", "Contact added!")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter all details")

def view_contacts():
    listbox.delete(0, tk.END)
    if not contacts:
        listbox.insert(tk.END, "No contacts found")
    else:
        for name, phone in contacts.items():
            listbox.insert(tk.END, f"{name} : {phone}")

def search_contact():
    name = entry_name.get()
    listbox.delete(0, tk.END)

    if name in contacts:
        listbox.insert(tk.END, f"{name} : {contacts[name]}")
    else:
        listbox.insert(tk.END, "Contact not found")

def delete_contact():
    name = entry_name.get()

    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", "Contact removed")
    else:
        messagebox.showwarning("Error", "Contact not found")

# Window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Labels & Entries
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()