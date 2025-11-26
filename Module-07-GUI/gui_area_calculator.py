"""
GUI Area Calculator using Tkinter.
Calculates area of rectangle.
"""

import tkinter as tk


def calculate_area():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        area = length * width
        label_result.config(text=f"Area = {area:.2f}")
    except ValueError:
        label_result.config(text="Enter valid numbers")


root = tk.Tk()
root.title("Rectangle Area Calculator")

tk.Label(root, text="Length:").grid(row=0, column=0, padx=5, pady=5)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Width:").grid(row=1, column=0, padx=5, pady=5)
entry_width = tk.Entry(root)
entry_width.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Calculate", command=calculate_area).grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
