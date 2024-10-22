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

def center_window(event=None):
    width = 400
    height = 600
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

sit_count = load_count()

root = tk.Tk()
root.title("DarkRP Sit Counter")
root.geometry("400x600")
root.configure(bg="black")

instruction_text = """This is a sit counter made for DarkRP.
Sometimes people don't have a lot of time to do sits, yet they are required to do a specific number of sits a week so they can keep helping the server.
This tool helps you to track your progress. When you accept a sit, simply press the button to keep count."""
instruction_label = tk.Label(root, text=instruction_text, wraplength=380, justify="center", bg="black", fg="white", font=("Segoe UI", 10))
instruction_label.pack(pady=20)

label_count = tk.Label(root, text=str(sit_count), font=("Segoe UI", 48), bg="black", fg="white")
label_count.pack(pady=20)

button_sit = tk.Button(root, text="Sit Opened", command=increment_count, bg="#282828", fg="white", font=("Segoe UI", 14), width=15)
button_sit.pack(pady=10)

button_reset = tk.Button(root, text="Reset Sit Count", command=reset_count, bg="#282828", fg="white", font=("Segoe UI", 14), width=15)
button_reset.pack(pady=10)

button_github = tk.Button(root, text="GitHub", command=open_github, bg="#282828", fg="white", font=("Segoe UI", 14), width=15)
button_github.pack(pady=10)

root.bind("<Configure>", center_window)

center_window()  # Center the window initially
root.mainloop()
