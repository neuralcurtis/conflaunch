import tkinter as tk
from tkinter import ttk
import subprocess

# File paths and labels
file_buttons = [
    ("Hyprland Config", "/home/ivan/.config/hypr/hyprland.conf"),
    ("Hyprlock Config", "/home/ivan/.config/hypr/hyprlock.conf"),
    ("Hyprpaper Config", "/home/ivan/.config/hypr/hyprpaper.conf"),
    ("Waybar JSON Config", "/etc/xdg/waybar/config.jsonc"),
    ("Waybar Style (CSS)", "/etc/xdg/waybar/style.css"),
    ("Neofetch Config", "/home/ivan/.config/neofetch/config.conf"),
]

def open_file_in_nvim(index):
    subprocess.Popen(['alacritty', '-e', 'nvim', file_buttons[index][1]])

# Initialize window
root = tk.Tk()
root.title("Neovim File Launcher")
root.geometry("460x480")
root.configure(bg="#1e1e2e")  # deep dark background

# Style configuration
style = ttk.Style(root)
style.theme_use("clam")

style.configure("Dark.TButton",
                foreground="#ffffff",
                background="#2e3440",
                font=("Segoe UI", 16, "bold"),
                padding=(10, 15),
                relief="flat")
style.map("Dark.TButton",
          background=[("active", "#3b4252")],
          foreground=[("pressed", "#a3be8c")])

# Title label
title = ttk.Label(root, text="Choose a config file to edit:",
                  background="#1e1e2e",
                  foreground="#d8dee9",
                  font=("Segoe UI", 18, "bold"))
title.pack(pady=(20, 15))

# Create buttons
for i, (label, _) in enumerate(file_buttons):
    btn = ttk.Button(root, text=label,
                     style="Dark.TButton",
                     command=lambda i=i: open_file_in_nvim(i))
    btn.pack(pady=6, ipadx=10, fill='x', padx=40)

root.mainloop()
