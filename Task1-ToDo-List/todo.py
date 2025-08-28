import tkinter as tk
from tkinter import messagebox

# ---------------- Functions ----------------
def add_task():
    task = task_entry.get().strip()
    if task != "":
        tasks_listbox.insert(tk.END, "📝 " + task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠ Warning", "Please enter a task!")

def delete_task():
    try:
        selected = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected)
    except:
        messagebox.showwarning("⚠ Warning", "Select a task to delete!")

def mark_done():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)
        tasks_listbox.delete(index)
        tasks_listbox.insert(tk.END, "✅ " + task.replace("📝 ", ""))
    except:
        messagebox.showwarning("⚠ Warning", "Select a task to mark done!")

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x450")
root.config(bg="#1e272e")

# Outer frame
outer_frame = tk.Frame(root, bg="#2f3640", bd=10, relief="ridge")
outer_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Header bar
header = tk.Label(
    outer_frame,
    text="✨ My To-Do List ✨",
    font=("Helvetica", 18, "bold"),
    bg="#00a8ff",
    fg="white",
    pady=10
)
header.pack(fill="x")

# Task entry box
task_entry = tk.Entry(outer_frame, width=30, font=("Helvetica", 13), bd=3, relief="solid")
task_entry.pack(pady=15)

# Button styles
btn_style = {
    "font": ("Helvetica", 11, "bold"),
    "width": 12,
    "bd": 0,
    "pady": 8,
    "cursor": "hand2"
}

btn_frame = tk.Frame(outer_frame, bg="#2f3640")
btn_frame.pack()

add_button = tk.Button(btn_frame, text="➕ Add", command=add_task, bg="#44bd32", fg="white", **btn_style)
add_button.grid(row=0, column=0, padx=8)

done_button = tk.Button(btn_frame, text="✔ Done", command=mark_done, bg="#0097e6", fg="white", **btn_style)
done_button.grid(row=0, column=1, padx=8)

delete_button = tk.Button(btn_frame, text="❌ Delete", command=delete_task, bg="#e84118", fg="white", **btn_style)
delete_button.grid(row=0, column=2, padx=8)

# Task list
tasks_listbox = tk.Listbox(
    outer_frame,
    width=45,
    height=12,
    font=("Helvetica", 13),
    bd=3,
    relief="solid",
    selectbackground="#9c88ff",
    activestyle="none"
)
tasks_listbox.pack(pady=15)

# Footer label
footer = tk.Label(
    outer_frame,
    text="* Designed by Aditi Maurya | Tkinter GUI *",
    font=("Helvetica", 10),
    bg="#2f3640",
    fg="lightgray"
)
footer.pack(side="bottom", pady=5)

root.mainloop()
