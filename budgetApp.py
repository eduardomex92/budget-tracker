"""
File: budgetApp.py
Heiner Alcala-Salas
Final Project: Budget Tracker
"""
import tkinter as tk
from tkinter import messagebox
from BudgetTracker import BudgetTracker

def main():
    tracker = BudgetTracker()

    while True:
        print("\n--- Budget Tracker Menu ---")
        print("1. Add income")
        print("2. Add expense")
        print("3. View total balance (Income and Remaining Balance)")
        print("4. Add a category")
        print("5. Remove a category")
        print("6. List categories")
        print("7. Quit")

        choice = input("Choose an option from the menu: ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter the income amount: ").strip())
                print(tracker.add_income(amount))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            category_name = input("Enter the category of the expense: ").strip()
            try:
                amount = float(input("Enter the expense amount: ").strip())
                # validate and make sure category exists
                if category_name not in tracker.categories:
                    print("Adding category: " + category_name)
                    tracker.add_category(category_name)  # Create the category if it doesn't exist
                print(tracker.add_expense(amount, category_name))  # Add expense to the category
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "3":
            total_balance = tracker.get_total_balance()     #gets total balance and stores them in variable
            print("Total Income: $" + "%.2f" % total_balance['income'])
            print("Remaining Balance: $" + "%.2f" % total_balance['remaining_balance'])
            print("Total expenses: $" + "%.2f" % total_balance['total_expenses'])

        elif choice == "4":
            name = input("Add new category: ").strip()
            print(tracker.add_category(name))       #passes name of category to be validated and created

        elif choice == "5":
            name = input("Enter the name of the category to remove: ").strip()
            print(tracker.remove_category(name))

        elif choice == "6":
            print(tracker.list_categories())

        elif choice == "7":
            print("Goodbye! See you soon.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
