import tkinter as tk

# ---------------- Functions ----------------
def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set(entry_var.get()[:-1])  # remove last character

def all_clear():
    entry_var.set("")

def evaluate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="lightgray")

# Center container
container = tk.Frame(root, bg="white", bd=5, relief="ridge")
container.pack(pady=20)
container.place(relx=0.5, rely=0.45, anchor="center")

# Display
entry_var = tk.StringVar()
entry = tk.Entry(container, textvariable=entry_var, font=("Arial", 20), bd=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons style
btn_params = {"padx":20, "pady":15, "bd":3, "font":("Arial",12,"bold")}

# AC and Clear row
tk.Button(container, text="AC", bg="tomato", fg="white", command=all_clear, **btn_params).grid(row=1, column=0, columnspan=2, sticky="nsew")
tk.Button(container, text="CLEAR", bg="orange", fg="white", command=clear, **btn_params).grid(row=1, column=2, columnspan=2, sticky="nsew")

# Number and operator buttons
buttons = [
    ('7',2,0), ('8',2,1), ('9',2,2), ('/',2,3),
    ('4',3,0), ('5',3,1), ('6',3,2), ('*',3,3),
    ('1',4,0), ('2',4,1), ('3',4,2), ('-',4,3),
    ('.',5,0), ('0',5,1), ('=',5,2), ('+',5,3)
]

for (text, row, col) in buttons:
    if text == "=":
        action = evaluate
        color = "green"
    elif text in {"+","-","*","/"}:
        action = lambda x=text: press(x)
        color = "skyblue"
    else:
        action = lambda x=text: press(x)
        color = "lightgray"
    
    tk.Button(container, text=text, bg=color, command=action, **btn_params).grid(row=row, column=col, sticky="nsew")

# Make buttons expand
for i in range(6):
    container.grid_rowconfigure(i, weight=1)
for j in range(4):
    container.grid_columnconfigure(j, weight=1)

root.mainloop()
