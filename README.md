# vityarthi_project
Expense Tracker (Python CLI Application)

A simple and efficient command-line Expense Tracker built in Python.
This application helps users record daily expenses, categorize them, search through them, and generate summary reports.
All data is stored persistently in a text file (expenses.txt).

Features
>Add new expenses
>View all recorded expenses
>Search expenses by category
>Summary report
>Total expenses
>Highest & lowest expense
>Category-wise totals
>Automatic loading & saving of data
>Uses a plain text file as a database (expenses.txt)

Technologies / Tools Used
>Python 3.x
>os module for file handling
>Text file storage (No external database required)

How to Use the Application_:
Once the program runs, you will see the main menu:
#Add Expense
 >Enter the amount spent
 >Enter category (Food / Travel / Shopping / Other)
 >Enter a short description
#View All Expenses
  Shows all stored expenses in this format;
  >₹120 - Food - Breakfast
#Search by Category
  Enter a category name → Lists matching expenses.
#Summary Report
Shows:
>Total money spent
>Highest & lowest expense
>Category-wise breakdown
#Exit
 Saves all data
 Closes the application

Code Structure & Logic:

~load_expenses()
Loads data from file into a list of dictionaries.
~save()
Writes all records back to the file when the user exits.
~add_entry()
Takes user input and adds a new expense.
~show_expenses()
Displays all expenses with index numbers.
~category()
Searches expense list for matching category names.
~report_summary()
Calculates:
Total expenses (sum())
Highest & lowest spend
Category-wise totals using a dictionary
~main_menu()
Controls all user navigation and handles choices.
