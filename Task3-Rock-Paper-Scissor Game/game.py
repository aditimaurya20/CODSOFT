import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    choice_text.set(f"You chose: {user_choice}   |   Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_text.set("🤝 Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text.set(f"✅ You Win! {user_choice} beats {computer_choice}")
        user_score += 1
    else:
        result_text.set(f"❌ You Lose! {computer_choice} beats {user_choice}")
        computer_score += 1

    score_text.set(f"🔹 You: {user_score}   🔸 Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    choice_text.set("Make your move!")
    result_text.set("Game Reset 🎮")
    score_text.set("🔹 You: 0   🔸 Computer: 0")

def exit_game():
    root.destroy()

# Main Window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("500x450")
root.config(bg="#D6EAF8")

# ---------- Container Frame ----------
container = tk.Frame(root, bg="white", bd=3, relief="ridge")
container.place(relx=0.5, rely=0.5, anchor="center", width=650, height=400)

# Title
title = tk.Label(container, text="✨ Rock - Paper - Scissors ✨",
                 font=("Arial", 18, "bold"), fg="white", bg="#5DADE2", pady=8)
title.pack(fill="x")

# Choices Display
choice_text = tk.StringVar()
choice_text.set("Make your move!")
choice_display = tk.Label(container, textvariable=choice_text,
                          font=("Arial", 12), bg="white", fg="#34495E", pady=10)
choice_display.pack()

# Result
result_text = tk.StringVar()
result_text.set("Choose Rock, Paper, or Scissors to start!")
result_label = tk.Label(container, textvariable=result_text,
                        font=("Arial", 12, "bold"), bg="white", fg="#2C3E50", pady=5)
result_label.pack()

# Score
score_text = tk.StringVar()
score_text.set("🔹 You: 0   🔸 Computer: 0")
score_label = tk.Label(container, textvariable=score_text,
                       font=("Arial", 13, "bold"), bg="white", fg="#2E4053", pady=10)
score_label.pack()

# Buttons
button_frame = tk.Frame(container, bg="white")
button_frame.pack(pady=15)

tk.Button(button_frame, text="✊ Rock", width=12, bg="#FAD7A0", font=("Arial", 12, "bold"),
          command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="✋ Paper", width=12, bg="#ABEBC6", font=("Arial", 12, "bold"),
          command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="✌ Scissors", width=12, bg="#F5B7B1", font=("Arial", 12, "bold"),
          command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Reset & Exit
bottom_frame = tk.Frame(container, bg="white")
bottom_frame.pack(pady=15)

tk.Button(bottom_frame, text="🔄 Reset", width=12, bg="#F39C12", fg="white",
          font=("Arial", 11, "bold"), command=reset_game).grid(row=0, column=0, padx=15)
tk.Button(bottom_frame, text="❌ Exit", width=12, bg="#C0392B", fg="white",
          font=("Arial", 11, "bold"), command=exit_game).grid(row=0, column=1, padx=15)

root.mainloop()
