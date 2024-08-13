import re
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, messagebox

def assess_password_strength(password):
    """
    Assesses the strength of the password based on length, presence of uppercase
    and lowercase letters, numbers, and special characters.
    """
    strength = 0
    feedback = []

    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Length criteria
    if length_criteria:
        strength += 1
    else:
        feedback.append("⚠️ Your password needs to be at least 8 characters long!")

    # Uppercase letter criteria
    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("⚠️ Don’t forget to use at least one uppercase letter!")

    # Lowercase letter criteria
    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("⚠️ Remember to include at least one lowercase letter!")

    # Digit criteria
    if digit_criteria:
        strength += 1
    else:
        feedback.append("⚠️ Your password needs at least one number!")

    # Special character criteria
    if special_char_criteria:
        strength += 1
    else:
        feedback.append("⚠️ Add at least one special character like !, @, or #!")

    # Determine the password strength level
    if strength == 5:
        feedback.append("🎉 Password strength: Super Strong! 💪")
        color = "limegreen"
        meter_color = "limegreen"
    elif strength == 4:
        feedback.append("👍 Password strength: Strong! 😃")
        color = "purple"
        meter_color = "purple"
    elif strength == 3:
        feedback.append("🙂 Password strength: Manageable! 😅")
        color = "black"
        meter_color = "black"
    elif strength == 2:
        feedback.append("😟 Password strength: Weak! 🥺")
        color = "orange"
        meter_color = "orange"
    else:
        feedback.append("❌ Password strength: Very Weak! 🚨")
        color = "red"
        meter_color = "red"

    return feedback, color, meter_color

def update_feedback(event=None):
    password = password_entry.get()
    feedback, color, meter_color = assess_password_strength(password)
    feedback_text = "\n".join(feedback)
    feedback_label.config(text=feedback_text, fg=color)

    # Update the strength meter
    meter_label.config(bg=meter_color)

def toggle_password_visibility():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        visibility_button.config(text='Hide Password')
    else:
        password_entry.config(show='*')
        visibility_button.config(text='Show Password')

def show_password_tips():
    tips = (
        "TIPS FOR CREATING STRONG PASSWORDS:\n\n"
        "1. Use a Mix of Characters: Include uppercase letters, lowercase letters, numbers, and special characters.\n"
        "2. Make It Long: Aim for at least 12 characters.\n"
        "3. Avoid Common Words: Avoid using easily guessable words or phrases.\n"
        "4. Use Passphrases: Combine random words or a phrase that's easy to remember but hard to guess.\n"
        "5. Change Regularly: Update your passwords regularly and avoid reusing old passwords.\n"
        "6. Consider a Password Manager: Use a password manager to generate and store complex passwords."
    )
    messagebox.showinfo("Password Tips", tips)

# Create the main window
root = tk.Tk()
root.title("PASSWORD STRENGTH CHECKER")
root.geometry("700x750")
root.configure(bg="#f0f8ff")

# Load cartoon images

lock_img = PhotoImage(file="lock.png")

# Create and place the widgets
title_label = tk.Label(root, text="🛡️ Password Strength Checker   🛡️", font=("Comic Sans MS", 24, "bold"), fg="#1e90ff",
                       bg="#f0f8ff")
title_label.pack(pady=20)



# Placing the lock image below the title
lock_label = tk.Label(root, image=lock_img, bg="#f0f8ff")
lock_label.pack(pady=(10, 0))

# Add the tips button immediately after the lock image
tips_button = tk.Button(root, text="Password Tips", font=("Comic Sans MS", 14), command=show_password_tips,
                        bg="#1e90ff", fg="#ffffff")
tips_button.pack(pady=(10, 10))

# Password entry and feedback
password_label = tk.Label(root, text="✍️ Enter Your Password ✍️️", font=("Comic Sans MS", 18, "bold"), fg="#4682b4",
                          bg="#f0f8ff")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=20, font=("Comic Sans MS", 19))
password_entry.pack(pady=10)
password_entry.bind("<KeyRelease>", update_feedback)

# Add the visibility toggle button
visibility_button = tk.Button(root, text="Show Password", font=("Comic Sans MS", 14),
                              command=toggle_password_visibility, bg="#1e90ff", fg="#ffffff")
visibility_button.pack(pady=(0, 5))  # Reduced space to 5 pixels

feedback_label = tk.Label(root, text="", font=("Comic Sans MS", 14), fg="#4682b4", bg="#f0f8ff", justify="left")
feedback_label.pack(pady=10)

# Add the password strength meter
meter_label = tk.Label(root, text="Password Strength Meter", font=("Comic Sans MS", 16, "bold"), bg="SKYBLUE", fg="white",
                       width=30, height=2)
meter_label.pack(pady=(0, 20))  # Increased space to 20 pixels to separate from feedback label



# Style configuration
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Comic Sans MS", 16, "bold"), foreground="#ffffff", background="#1e90ff",
                borderwidth=0, focusthickness=3, focuscolor='none')
style.map("TButton", background=[('active', '#1e90ff')], foreground=[('active', '#ffffff')])

# Run the application
root.mainloop()
