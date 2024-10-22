import tkinter as tk
import os

def save_count(count):
    with open("sit_count.txt", "w") as file:
        file.write(str(count))

def load_count():
    if os.path.exists("sit_count.txt"):
        with open("sit_count.txt", "r") as file:
            try:
                return int(file.read())
            except ValueError:
                return 0
    return 0

def increment_count():
    global sit_count
    sit_count += 1
    label_count.config(text=str(sit_count))
    save_count(sit_count)

def reset_count():
    global sit_count
    sit_count = 0
    label_count.config(text=str(sit_count))
    save_count(sit_count)

def open_github():
    import webbrowser
    webbrowser.open("https://github.com/Funstab")

def center_window():
    width = 400
    height = 600
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

sit_count = load_count()

root = tk.Tk()
root.title("DarkRP Sit Counter")
root.configure(bg="#030413")

# Center the window initially
center_window()

instruction_text = """This is a sit counter made for DarkRP.
Sometimes people don't have a lot of time to do sits, yet they are required to do a specific number of sits a week so they can keep helping the server.
This tool helps you to track your progress. When you accept a sit, simply press the button to keep count."""
instruction_label = tk.Label(root, text=instruction_text, wraplength=380, justify="center", bg="#030413", fg="white", font=("Segoe UI", 10))
instruction_label.pack(pady=20)

label_count = tk.Label(root, text=str(sit_count), font=("Segoe UI", 48), bg="#030413", fg="white")
label_count.pack(pady=20)

def create_modern_button(parent, text, command, bg_color):
    button = tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg_color,
        fg='white',
        font=("Segoe UI", 14),
        borderwidth=0,
        activebackground='#3a3a4f',
        relief='flat'
    )
    button.pack(pady=10, padx=20)
    button.config(highlightbackground="#030413", highlightthickness=0)
    button.bind("<Enter>", lambda e: button.config(bg=bg_color))
    button.bind("<Leave>", lambda e: button.config(bg=bg_color))
    return button

button_sit = create_modern_button(root, "Sit Opened", increment_count, '#a12cad')
button_reset = create_modern_button(root, "Reset Sit Count", reset_count, '#c1667a')
button_github = create_modern_button(root, "GitHub", open_github, '#c40874')

root.mainloop()
