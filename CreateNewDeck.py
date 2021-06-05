# All the code for creating a new deck
import os
import tkinter as tk
from functools import partial


def destroy_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def print_hi():
    print("hi")


def create_new_deck(frame):
    deck_frame = tk.Frame(frame, bg="light blue")
    deck_frame.place(relwidth=0.9, relx=0.05, rely=0.07)

    deck_name_lbl = tk.Label(deck_frame, text="Deck Name: ", pady=5, padx=10, bg="light blue")
    deck_name_lbl.pack(side="left")

    text_field = tk.Entry(deck_frame)
    text_field.pack(side="left")
    text_field.focus_set()

    submit_btn = tk.Button(deck_frame, text="Submit", padx=10, pady=0, width=7,
                           fg="white", bg="#263D42", command=lambda: submit_name(text_field.get(), deck_frame))
    submit_btn.pack(pady=3, side="bottom")


def submit_name(name, frame):
    destroy_widgets(frame)
    deck_name_lbl = tk.Label(frame, text=name, pady=5, padx=10, bg="light blue")
    deck_name_lbl.pack(side="left")
