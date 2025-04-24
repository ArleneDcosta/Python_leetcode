import pandas as pd
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Initialize CSV if not exists
def init_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(FILE_NAME, index=False)

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (e.g. Food, Rent, Transport): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description (optional): ")

    df = pd.read_csv(FILE_NAME)
    df = df.append({
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }, ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("Expense added successfully!\n")

# View all expenses
def view_expenses():
    df = pd.read_csv(FILE_NAME)
    print("\nAll Expenses:")
    print(df)

# Filter expenses by date or category
def filter_expenses():
    df = pd.read_csv(FILE_NAME)
    choice = input("Filter by (1) Date or (2) Category? ")
    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        filtered = df[df['Date'] == date]
    elif choice == '2':
        category = input("Enter category: ")
        filtered = df[df['Category'].str.lower() == category.lower()]
    else:
        print("Invalid choice.")
        return
    print(filtered)

# Show summary of expenses
def summary():
    df = pd.read_csv(FILE_NAME)
    total = df['Amount'].sum()
    by_category = df.groupby('Category')['Amount'].sum()
    print("\nTotal Expenses: $", total)
    print("\nExpenses by Category:")
    print(by_category)

# Main loop
def main():
    init_file()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Summary")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_expenses()
        elif choice == '4':
            summary()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
