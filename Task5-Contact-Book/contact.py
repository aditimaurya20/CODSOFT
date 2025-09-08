import tkinter as tk
from tkinter import messagebox

contacts = {}  # Dictionary to store contacts

def add_contact_form():
    form = tk.Toplevel(root)
    form.title("Add Contact")
    form.geometry("350x450")
    form.configure(bg="#f2f2f2")

    tk.Label(form, text="Name:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
    entry_name = tk.Entry(form, font=("Arial", 12), width=25)
    entry_name.pack()

    tk.Label(form, text="Phone:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
    entry_phone = tk.Entry(form, font=("Arial", 12), width=25)
    entry_phone.pack()

    tk.Label(form, text="Email:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
    entry_email = tk.Entry(form, font=("Arial", 12), width=25)
    entry_email.pack()

    tk.Label(form, text="Address:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
    entry_address = tk.Entry(form, font=("Arial", 12), width=25)
    entry_address.pack()

    def save_contact():
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required!")
            return

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        messagebox.showinfo("Success", "Contact added successfully!")
        form.destroy()

    tk.Button(form, text="Save", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
              width=15, command=save_contact).pack(pady=15)


# ---------------- Update Contact Form ---------------- #
def update_contact_form():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to update.")
        return
    name = contact_list.get(selected[0]).split(" - ")[0]

    form = tk.Toplevel(root)
    form.title("Update Contact")
    form.geometry("350x300")
    form.configure(bg="#f2f2f2")

    tk.Label(form, text="Name:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
    entry_name = tk.Entry(form, font=("Arial", 12), width=25)
    entry_name.insert(0, name)
    entry_name.pack()

    tk.Label(form, text="Phone:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
    entry_phone = tk.Entry(form, font=("Arial", 12), width=25)
    entry_phone.insert(0, contacts[name]["Phone"])
    entry_phone.pack()

    tk.Label(form, text="Email:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
    entry_email = tk.Entry(form, font=("Arial", 12), width=25)
    entry_email.insert(0, contacts[name]["Email"])
    entry_email.pack()

    tk.Label(form, text="Address:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
    entry_address = tk.Entry(form, font=("Arial", 12), width=25)
    entry_address.insert(0, contacts[name]["Address"])
    entry_address.pack()

    def save_update():
        new_name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()

        if not new_name or not phone:
            messagebox.showerror("Error", "Name and Phone are required!")
            return

        # If name changed, remove old entry
        if new_name != name:
            del contacts[name]

        contacts[new_name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        messagebox.showinfo("Success", "Contact updated successfully!")
        form.destroy()

    tk.Button(form, text="Update", bg="#FFC107", fg="black", font=("Arial", 12, "bold"),
              width=15, command=save_update).pack(pady=15)


# ---------------- Delete Contact ---------------- #
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return
    name = contact_list.get(selected[0]).split(" - ")[0]
    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {name}?")
    if confirm:
        del contacts[name]
        update_contact_list()


# ---------------- Search Contact ---------------- #
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        if query in name.lower() or query in info["Phone"]:
            contact_list.insert(tk.END, f"{name} - {info['Phone']}")


# ---------------- Update Contact List ---------------- #
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['Phone']}")


# ---------------- Main Window ---------------- #
root = tk.Tk()
root.title("Contact Book")
root.geometry("300x450")
root.configure(bg="#f2f2f2")

title_label = tk.Label(root, text="Contact Book", font=("Arial", 20, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)

# Search bar
search_frame = tk.Frame(root, bg="#f2f2f2")
search_frame.pack(pady=5)
search_entry = tk.Entry(search_frame, font=("Arial", 12), width=30)
search_entry.pack(side=tk.LEFT, padx=5)
search_btn = tk.Button(search_frame, text="Search", bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                       command=search_contact)
search_btn.pack(side=tk.LEFT)

# Contact list
frame = tk.Frame(root, bd=3, relief="groove", bg="white")
frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

contact_list = tk.Listbox(frame, font=("Arial", 12), height=12, width=50)
contact_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=contact_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
contact_list.config(yscrollcommand=scrollbar.set)

# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=15)

btn_add = tk.Button(button_frame, text="➕ Add", width=12, height=2, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
                    command=add_contact_form)
btn_add.grid(row=0, column=0, padx=10)

btn_update = tk.Button(button_frame, text="✏️ Update", width=12, height=2, bg="#FFC107", fg="black", font=("Arial", 12, "bold"),
                       command=update_contact_form)
btn_update.grid(row=0, column=1, padx=10)

btn_delete = tk.Button(button_frame, text="🗑️ Delete", width=12, height=2, bg="#F44336", fg="white", font=("Arial", 12, "bold"),
                       command=delete_contact)
btn_delete.grid(row=0, column=2, padx=10)

root.mainloop()

