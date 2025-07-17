import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x500")
root.configure(bg="#1e1e1e")  # Dark background

# Variables for scores
user_score = 0
computer_score = 0

# Fonts
FONT_TITLE = ("Helvetica", 20, "bold")
FONT_BUTTON = ("Helvetica", 14)
FONT_RESULT = ("Courier", 14, "bold")
FONT_SCORE = ("Helvetica", 13)

# Result Label
result_label = tk.Label(root, text="Choose your move!", fg="white", bg="#1e1e1e", font=FONT_RESULT)
result_label.pack(pady=20)

# Scoreboard
score_label = tk.Label(root, text=f"You: 0   |   Computer: 0", fg="lightgreen", bg="#1e1e1e", font=FONT_SCORE)
score_label.pack(pady=10)

# Update Scoreboard
def update_scoreboard():
    score_label.config(text=f"You: {user_score}   |   Computer: {computer_score}")

# Game Logic
def play(user_choice):
    global user_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = f"Draw! Both chose {user_choice}"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result = f"You Win! {user_choice} beats {computer_choice}"
        user_score += 1
    else:
        result = f"You Lose! {computer_choice} beats {user_choice}"
        computer_score += 1

    result_label.config(text=result)
    update_scoreboard()

# Buttons
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, height=2, bg="#4e4eff", fg="white", font=FONT_BUTTON,
                        command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, height=2, bg="#00c853", fg="white", font=FONT_BUTTON,
                         command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, height=2, bg="#ff1744", fg="white", font=FONT_BUTTON,
                            command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Run the GUI loop
root.mainloop()
