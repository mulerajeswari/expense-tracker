import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Create file with headers if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if not category or not amount:
        messagebox.showerror("Error", "Category and Amount are required!")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    messagebox.showinfo("Success", "Expense added successfully!")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    view_expenses()

def view_expenses():
    for row in tree.get_children():
        tree.delete(row)

    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                tree.insert("", tk.END, values=row)

# GUI setup
root = tk.Tk()
root.title("💰 Expense Tracker")
root.geometry("700x500")
root.config(bg="white")

# Input Frame
input_frame = tk.Frame(root, bg="white", pady=10)
input_frame.pack()

tk.Label(input_frame, text="Category:", bg="white").grid(row=0, column=0, padx=5, pady=5)
category_entry = tk.Entry(input_frame)
category_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Amount:", bg="white").grid(row=0, column=2, padx=5, pady=5)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(input_frame, text="Description:", bg="white").grid(row=0, column=4, padx=5, pady=5)
description_entry = tk.Entry(input_frame)
description_entry.grid(row=0, column=5, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=6, padx=5, pady=5)

# Table Frame
table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

columns = ("Date", "Category", "Amount", "Description")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER, width=150)
tree.pack(fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

view_expenses()

root.mainloop()
