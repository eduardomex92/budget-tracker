"""
File: BudgetTracker.py
Heiner Alcala-Salas
Final Project: Budget Tracker
"""
import os
import json
from Category import Category

class BudgetTracker:
    """Manages multiple budget categories."""

    def __init__(self, filename = "budget_data.json"):
        """Initializes the tracker with an empty dictionary of categories."""
        self.categories = {}            # initialize empty dict to store categories
        self.total_income = 0           # Track total income globally
        self.accumulate_income = 0      # Tracks total accumulated income
        self.filename = filename        # set filename to save and load it
        self.verify_file()              # validates if file exist
        self.load_data()                # Loads data from file

    def verify_file(self):
        """checks if file exists, creates it if not."""
        if not os.path.exists(self.filename):                       # checks if file exists
            print("Data file not found. Creating a new one...")     # display message if file does not exist
            f = open(self.filename, 'w')        #creates file in write mode
            json.dump({"categories": {}, "total_income": 0, "accumulate_income": 0}, f) # prepares file with and empty structe 
            f.close()       #closes file

    def load_data(self):
        """Loads data from the file into the tracker."""
        file = open(self.filename, 'r')     # opens file in read mode
        data = json.load(file)              # load JSON data from file
        file.close()                        # closes file

        self.total_income = data["total_income"]            # sets total income value from data
        self.accumulate_income = data["accumulate_income"]  # sets accumulated income from data

        #converts categories from dictionaries to Category objects
        for name, info in data["categories"].items():
            category = Category(name)               #creates a new category object for each category
            category.expenses = info["expenses"]    # sets the expenses for the categories
            self.categories[name] = category        # add the category to tracker


    def save_data(self):
        """Saves the current changes of the tracker to the file.
        I had to find a way to change the object into a seriaziable format in order to save back into the file """
        serializable_categories = {
            name: {
                "expenses": category.expenses
            }
            for name, category in self.categories.items()
        }
        data = {
            "categories": serializable_categories,
            "total_income": self.total_income,
            "accumulate_income": self.accumulate_income
        }
        file = open(self.filename, 'w')  # Open the file in write mode
        json.dump(data, file)            # Write the JSON data
        file.close()                     # Close the file

    def add_income(self, amount):
        """Add income to the tracker"""
        if amount <= 0:                                         # if amount is less than or equal to 0, returns error message
            return "Income amount must be greater than 0."
        self.total_income += amount                             # adds amount to total_income
        self.accumulate_income += amount                        # adds amount to a accumulate_income var
        self.save_data()                                        # saves data to file
        return "Added income of $" + "%.2f" % amount + ".\n"    #returns confirmation message

    def add_expense(self, amount, category_name):
        """Add expense to a category and subtract from total balance"""
        if amount <= 0:                                         # validates amount is greater than 0
            return "Expense amount must be greater than 0."     # returns message
        elif amount > self.total_income:                        # if expense amount is greated than total income, returns error message
            return "Insufficient funds."
        if category_name not in self.categories:
            return "Category does not exist."                    # fallback that validates if the category exists
        self.total_income -= amount                                     #subtracts expenses amount from total income to get actual balance 
        result = self.categories[category_name].add_expense(amount)     # saves the categorie along with the expense, stores them into variable
        self.save_data()                                                # saves data
        return result   #returns result


    def get_total_balance(self):
        """Get the total income and remaining balance."""
        total_expenses = 0              #initializes total expenses
        for category in self.categories.values():
            total_expenses += category.get_total_expenses()     # loops through values(amount for each category) and adds them into total_expenses
        remaining_balance = self.total_income                   # imports total_income value and sets it in remaining_balance 
        return {
            'income': self.accumulate_income,                   #returns values to be displayed in account details
            'remaining_balance': remaining_balance,
            'total_expenses': total_expenses
        }

    def add_category(self, name):
        """Add a new category"""
        name = name.strip().lower()                 # makes category noncase sensitive
        if name in self.categories:                 #checks for existing category
            return "Category already exists."       # fallback, returns message confirming category already exists
        self.categories[name] = Category(name)      # else creates category, sends name parameter to category class
        self.save_data()
        return "Category " + name + " added."       # returns confirmation message

    def remove_category(self, name):
        """remove a category"""
        name = name.strip().lower()                                     #makes category noncase sensitive
        if name not in self.categories:                                 # checks if catefory exist, if not returns error message
            return "Category does not exist."
        total_expenses = self.categories[name].get_total_expenses()     # Retrieves the total expense of the category to be removed
        self.total_income += total_expenses                             # Adds those expenses back to the total income
        del self.categories[name]                                       #deletes category with matching name
        self.save_data()
        return "Category " + name + " was successfully removed, and $" + "%.2f" % total_expenses + " was restored to your balance." #returns confirmation message

    def list_categories(self):
        """List all categories"""
        if not self.categories:     # if categories is empty, returns message
            return "No categories to display"
        display_list = []                   #initializes empty list to store category names
        for category in self.categories.values():   #loops through the categoris
            display_list.append(str(category))  # add each category converts it to string representation to the list
    
        return "\n".join(display_list)  #join all category strings with newlines



