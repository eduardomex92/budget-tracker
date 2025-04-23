"""
File: Category.py
Heiner Alcala-Salas
Final project: Budget Tracker
"""
class Category:
    """Represents a budget category."""
    def __init__(self, name):
        """initialize category with name and empty list of expenses."""
        self.name = name        #stores name of category
        self.expenses = []      #holds expenses link to category

    def add_expense(self, amount):
        """Add an expense to the category."""
        if amount <= 0:         #validates amount if is less than or equal to 0
            return "Expense amount must be greater than 0."
        self.expenses.append(amount)            #else, adds amount
        return "Added expense of $" + "%.2f" % amount + " to category: " + self.name
        
    def get_total_expenses(self):
        """Returns the total expenses for this category"""
        return sum(self.expenses)

    def __str__(self):
        """return string representing categories with their total expenses"""
        return self.name + " - Total Expenses: $" + "%.2f" % self.get_total_expenses()


