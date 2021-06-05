# All the code for creating a new deck
import os
import tkinter as tk


def print_hi():
    print("hi")


def create_new_deck(frame):
    subtitle = tk.Label(frame, text="Create New Deck", pady=5, padx=10, bg="light blue")
    subtitle.pack()

    deck_name_lbl = tk.Label(frame, text="Deck Name: ", pady=5, padx=10, bg="light blue")
    deck_name_lbl.pack()

    submit_btn = tk.Button(frame, text="Submit", padx=10, pady=5, width=10,
                                    fg="white", bg="#263D42", command=print_hi)
    submit_btn.pack(pady=3)
