Expense Tracker (Python + Tkinter)
This is a simple desktop app I made to keep track of my daily expenses.
It’s built with Python and Tkinter, and it stores all the data in a CSV file so I can see my records anytime.

What it does
Lets you add an expense with:

Category (Food, Travel, Shopping, etc.)

Amount

Description (optional)

Saves the date & time automatically.

Shows all the expenses in a neat table.

Keeps the data safe in a CSV file so it doesn’t get lost when you close the app.

How to run it
Make sure you have Python 3 installed.
Check with:

css
Copy
Edit
python --version
Tkinter comes pre-installed with Python, so no extra library is needed.

Save the Python file as expense_tracker.py.

Just run:

nginx
Copy
Edit
python expense_tracker.py
How it stores data
The app saves everything in a file called expenses.csv.
Here’s an example of what it looks like:

yaml
Copy
Edit
Date,Category,Amount,Description
2025-08-09 10:32:21,Food,200,Lunch
2025-08-09 14:12:05,Travel,100,Bike fuel
Why I made it
I wanted something quick and simple to record where my money goes without using big software or online tools.
This app is small, portable, and does the job.
