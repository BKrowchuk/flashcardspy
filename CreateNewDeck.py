# All the code for creating a new deck
import os
import tkinter as tk
from tkinter import ttk


def destroy_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def scroll_region(canvas):
    canvas.configure(scrollregion=canvas.bbox('all'))


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

    # Static info
    # Deck name display
    frame1 = tk.Frame(frame, bg="light blue")
    frame1.pack(fill="x")
    deck_name_lbl = tk.Label(frame1, text="Deck Name: "+name, pady=5, padx=10, bg="light blue")
    deck_name_lbl.pack(side="left")

    # Section Title
    frame2 = tk.Frame(frame, bg="light blue")
    frame2.pack(fill="x")
    add_items_lbl = tk.Label(frame2, text="Add Items", pady=5, padx=10, bg="light blue")
    add_items_lbl.pack(side="left")

    # Add Area
    frame3 = tk.Frame(frame, bg="light blue")
    frame3.pack(fill="x")
    side_1_lbl = tk.Label(frame3, text="Side 1:", pady=5, padx=10, bg="light blue")
    side_1_lbl.pack(side="left")
    text_field_1 = tk.Entry(frame3)
    text_field_1.pack(side="left")
    text_field_1.focus_set()
    side_2_lbl = tk.Label(frame3, text="Side 2:", pady=5, padx=10, bg="light blue")
    side_2_lbl.pack(side="left")
    text_field_2 = tk.Entry(frame3)
    text_field_2.pack(side="left")

    # Buttons
    frame4 = tk.Frame(frame, bg="light blue")
    frame4.pack(fill="x")
    finish_btn = tk.Button(frame4, text="Finish and Save", padx=10, pady=0, width=10,
                           fg="white", bg="#263D42", command=lambda: print("finished"))
    finish_btn.pack(pady=3, side="right")

    # Scrollable Frame
    wrapper = tk.Label(frame)
    canvas = tk.Canvas(wrapper)
    canvas.pack(side="left", fill="both", expand="yes")

    yscrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=canvas.yview)
    yscrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=yscrollbar.set)

    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    myframe = tk.Frame(canvas)
    canvas.create_window((0, 0), window=myframe, anchor='nw')

    wrapper.pack(fill="both")

    wrapper.pack(fill="both", expand="yes", padx=5, pady=5)

    for i in range(50):
        tk.Button(myframe, text="My Button - " + str(i)).pack()

    # Next Part
    frame5 = tk.Frame(myframe, bg="light blue")
    frame5.pack(fill="y", side="left")

    frame6 = tk.Frame(myframe, bg="light blue")
    frame6.pack(fill="y", side="right")
    side_1_lbl = tk.Label(frame5, text="Side 1", pady=5, padx=10, bg="light blue")
    side_1_lbl.pack()
    side_2_lbl = tk.Label(frame6, text="Side 2", pady=5, padx=10, bg="light blue")
    side_2_lbl.pack()

    # Second Button
    add_btn = tk.Button(frame4, text="Add", padx=10, pady=0, width=7,
                        fg="white", bg="#263D42",
                        command=lambda: add_item(frame5, frame6, text_field_1.get(), text_field_2.get()))
    add_btn.pack(pady=3, side="right")


def add_item(frame1, frame2, side1, side2):
    # List Items
    side_1_lbl = tk.Label(frame1, text=side1, pady=5, padx=10, bg="light blue")
    side_1_lbl.pack()
    side_2_lbl = tk.Label(frame2, text=side2, pady=5, padx=10, bg="light blue")
    side_2_lbl.pack()

