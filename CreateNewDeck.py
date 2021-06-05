# All the code for creating a new deck
import os
import tkinter as tk
from functools import partial


def print_hi():
    print("hi")


def create_new_deck(frame):
    deck_frame = tk.Frame(frame, bg="light blue")
    deck_frame.place(relwidth=0.9, relx=0.05, rely=0.05)

    subtitle = tk.Label(deck_frame, text="Create New Deck", pady=5, padx=10, bg="light blue")
    subtitle.pack()

    deck_name_lbl = tk.Label(deck_frame, text="Deck Name: ", pady=5, padx=10, bg="light blue")
    deck_name_lbl.pack(side="left")

    text_field = tk.Entry(deck_frame)
    text_field.pack(side="left")
    text_field.focus_set()

    submit_btn = tk.Button(deck_frame, text="Submit", padx=10, pady=0, width=7,
                           fg="white", bg="#263D42", command=lambda: submit_name(text_field.get()))
    submit_btn.pack(pady=3, side="bottom")


def submit_name(name):
    print(name)
