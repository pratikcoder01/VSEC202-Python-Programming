"""
Simple GUI unit converter using Tkinter.
Converts kilometers to miles.
"""

import tkinter as tk


def convert():
    try:
        km = float(entry_km.get())
        miles = km * 0.621371
        label_result.config(text=f"{miles:.2f} miles")
    except ValueError:
        label_result.config(text="Enter a valid number")


root = tk.Tk()
root.title("KM to Miles Converter")

tk.Label(root, text="Distance in kilometers:").pack(pady=5)
entry_km = tk.Entry(root)
entry_km.pack(pady=5)

tk.Button(root, text="Convert", command=convert).pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=5)

root.mainloop()
