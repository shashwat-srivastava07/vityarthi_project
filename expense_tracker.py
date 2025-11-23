import os
expense_list = []
DATA_FILE = "expenses.txt" 
def load_expenses():
    if os.path.exists(DATA_FILE):
        try:
            f = open(DATA_FILE, "r")
            for line in f:
                line = line.strip()
                parts = line.split("|")

                if len(parts) != 3:
                    print("Skipping malformed line:", line)
                    continue

                amount_s, cat, desc = parts

                amt = float(amount_s)

                expense_list.append({
                    "amount": amt,
                    "category": cat,
                    "description": desc
                })
            f.close()
        except Exception as e:
            print("Error reading file:", e)
    else:
        open(DATA_FILE, "w").close()


def save():
    try:
        with open(DATA_FILE, "w") as fh:
            for rec in expense_list:
                a = rec['amount']
                c = rec['category']
                d = rec['description']

                fh.write(f"{a}|{c}|{d}\n")
    except Exception as ex:
        print("Couldn't save data:", ex)

def add_entry():
    try:
        raw = input("Enter amount spent: ").strip()
        raw = raw.replace(",", "")
        amt = float(raw) if raw != "" else 0.0
    except Exception:
        print("Invalid amount entered — defaulting to 0.0")
        amt = 0.0

    cat = input("Enter category (Food/Travel/Shopping/Other): ").strip()
    if not cat:
        cat = "Other"

    desc = input("Enter short description: ").strip()
    if not desc:
        desc = "-"

    new_record = {"amount": amt, "category": cat, "description": desc}
    expense_list.append(new_record)
    print("\nExpense added successfully!\n")

def show_expenses():
    if not expense_list:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n----- ALL EXPENSES -----")
    idx = 1
    for exp in expense_list:
        print(f"{idx}. ₹{exp['amount']} - {exp['category']} - {exp['description']}")
        idx += 1
    print()

def category():
    query = input("Enter category to search: ").strip()
    qlow = query.lower()
    found = False

    print("\n----- SEARCH RESULTS -----")
    for exp in expense_list:
        if exp['category'].strip().lower() == qlow:
            print(f"₹{exp['amount']} - {exp['description']}")
            found = True

    if not found:
        print("No expenses found for this category.\n")

def report_summary():
    if not expense_list:
        print("\nNo data available to generate summary.\n")
        return

    total_amt = 0
    for item in expense_list:
        total_amt += item['amount'] 
    alt_total = sum([entry['amount'] for entry in expense_list])

    highest_spend = expense_list[0]
    lowest_spend = expense_list[0]
    for entry in expense_list:
        if entry['amount'] > highest_spend['amount']:
            highest_spend = entry
        if entry['amount'] < lowest_spend['amount']:
            lowest_spend = entry

    cat_total_map = {}
    for item in expense_list:
        cat_name = item['category']
        cat_total_map[cat_name] = cat_total_map.get(cat_name, 0.0) + float(item['amount'])

    print("\n----- SUMMARY REPORT -----")
    print(f"Total Expenses: ₹{total_amt:.2f}")
    print(f"Highest Expense: ₹{highest_spend['amount']} ({highest_spend['category']})")
    print(f"Lowest Expense: ₹{lowest_spend['amount']} ({lowest_spend['category']})")
    print("\nCategory-wise totals:")

    for cname, camt in cat_total_map.items():
        print(f"  {cname} : ₹{camt:.2f}")

    print()

    print("\n----- SUMMARY REPORT -----")
    print(f"Total Expenses: ₹{total_amt:.2f}")
    print(f"Highest Expense: ₹{highest_spend['amount']} ({highest_spend['category']})")
    print(f"Lowest Expense: ₹{lowest_spend['amount']} ({lowest_spend['category']})")
    print("\nCategory-wise totals:")

    for cname, camt in cat_total_map.items():
        print(f"  {cname} : ₹{camt:.2f}")
    print()

def main_menu():
    while True:
        print("===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Summary Report")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            category()
        elif choice == "4":
            report_summary()
        elif choice == "5":
            save()
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice! Try again.\n")

load_expenses()
main_menu()
