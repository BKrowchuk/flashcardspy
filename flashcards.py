import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title('Flashcards')
curr_file = ['default']


def open_deck():
    curr_file.pop()
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Deck",
                                          filetypes=(("text", "*.txt"), ("all files", "*.*")))
    for widget in deck_frame.winfo_children():
        widget.destroy()
    label = tk.Label(deck_frame, text=filename, pady=5, padx=10, bg="light blue")
    label.pack(side="left")
    curr_file.append(filename)


# bg="light blue"
canvas = tk.Canvas(root, height=600, width=700, bg="#263D42")
canvas.pack()

deck_frame = tk.Frame(root, height=100, width=100)
deck_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

open_file = tk.Button(root, text="Load Deck", padx=10,
                      pady=5, fg="white", bg="#263D42", command=open_deck)
open_file.pack()


root.mainloop()

with open('save.txt', 'w') as f:
    for file in curr_file:
        f.write(file)
