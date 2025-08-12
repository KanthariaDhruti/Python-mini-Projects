import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Create CSV file if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter amount: ₹"))
    description = input("Enter description: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("✅ Expense added successfully!")

def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("\n--- All Expenses ---")
        for row in reader:
            print(f"{row[0]} | {row[1]} | ₹{row[2]} | {row[3]}")

def total_expenses():
    total = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            total += float(row[2])
    print(f"\n💰 Total Expenses: ₹{total}")

def expenses_by_category():
    category_totals = {}
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[1]
            amount = float(row[2])
            category_totals[category] = category_totals.get(category, 0) + amount

    print("\n📊 Expenses by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ₹{total}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            expenses_by_category()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()