import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title('Leornian')
curr_file = ['default']
option_btn_padding = 3
options_widths = 17


# Option buttons functions
def destroy_widgets():
    for widget in user_frame.winfo_children():
        widget.destroy()


def add_label(label_text):
    label = tk.Label(user_frame, text=label_text, pady=5, padx=10, bg="light blue")
    label.pack()


def create_new_deck():
    destroy_widgets()
    add_label("create new deck clicked")


def load_deck():
    curr_file.pop()
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Deck",
                                          filetypes=(("text", "*.txt"), ("all files", "*.*")))
    destroy_widgets()
    curr_deck_lbl = tk.Label(user_frame, text=filename, pady=5, padx=10, bg="light blue")
    curr_deck_lbl.pack(side="left")
    curr_file.append(filename)


def practice():
    destroy_widgets()
    add_label("practice clicked")


def my_stats():
    destroy_widgets()
    add_label("my stats clicked")


# Creating canvas and title
# bg="light blue"
canvas = tk.Canvas(root, height=600, width=700, bg="#263D42")
canvas.pack()

title_frame = tk.Frame(root, bg="#263D42")
title_frame.place(relwidth=0.9, relheight=0.05, relx=0.05, rely=0.04)

title = tk.Label(title_frame, text="Leornian", fg="white", bg="#263D42")
title.pack()

# Creating frames for dashboard separation
options_frame = tk.Frame(root, bg="light blue")
options_frame.place(relwidth=0.27, relheight=0.85, relx=0.045, rely=0.1)

user_frame = tk.Frame(root, bg="light blue")
user_frame.place(relwidth=0.585, relheight=0.85, relx=0.37, rely=0.1)

# Populating options frame
options_lbl = tk.Label(options_frame, text="Options", fg="black", bg="light blue", width=options_widths)
options_lbl.pack(pady=option_btn_padding)

create_new_deck_btn = tk.Button(options_frame, text="Create New Deck", padx=10, pady=5, width=options_widths,
                                fg="white", bg="#263D42", command=create_new_deck)
create_new_deck_btn.pack(pady=option_btn_padding)

load_deck_btn = tk.Button(options_frame, text="Load Deck", padx=10, pady=5, width=options_widths,
                          fg="white", bg="#263D42", command=load_deck)
load_deck_btn.pack(pady=option_btn_padding)

practice_btn = tk.Button(options_frame, text="Practice", padx=10, pady=5, width=options_widths,
                         fg="white", bg="#263D42", command=practice)
practice_btn.pack(pady=option_btn_padding)

my_stats_btn = tk.Button(options_frame, text="My Stats", padx=10, pady=5, width=options_widths,
                         fg="white", bg="#263D42", command=my_stats)
my_stats_btn.pack(pady=option_btn_padding)

root.mainloop()

with open('save.txt', 'w') as f:
    for file in curr_file:
        f.write(file)
