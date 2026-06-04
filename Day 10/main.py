import csv
import os

FILENAME = "expenses.csv"

# Create file if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Description"])


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])

    print("Expense added successfully!\n")


def view_expenses():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    if len(data) <= 1:
        print("No expenses found.\n")
        return

    print("\n--- Expenses ---")
    for row in data[1:]:
        print(f"₹{row[0]} | {row[1]} | {row[2]}")
    print()


def total_expenses():
    total = 0

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expenses: ₹{total:.2f}\n")


def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()