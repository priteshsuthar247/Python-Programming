import tkinter as tk

def on_button_click():
    entered_age = entry.get()
    label_result.config(text=f"Your age is {entered_age}!")

window = tk.Tk()
window.title("Age Calculator")

window.configure(bg="black")

heading_label = tk.Label(window, text="Age Calculator", bg="black", fg="white", font=("Arial", 20))
heading_label.pack(pady=10)

label = tk.Label(window, text="Enter your age:", bg="black", fg="white", font=("Arial", 16))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(window, text="Submit", command=on_button_click, font=("Arial", 14))
button.pack(pady=10)

label_result = tk.Label(window, text="", bg="black", fg="white", font=("Arial", 16))
label_result.pack(pady=10)

window.mainloop()
