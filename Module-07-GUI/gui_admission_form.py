"""
Simple Admission Registration Form using Tkinter.
"""

import tkinter as tk
from tkinter import messagebox


def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()
    if not name or not age or not course:
        messagebox.showwarning("Missing Data", "Please fill all fields.")
        return
    messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nCourse: {course}")


root = tk.Tk()
root.title("Admission Form")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Course:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_course = tk.Entry(root)
entry_course.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Submit", command=submit_form).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
