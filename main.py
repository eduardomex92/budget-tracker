"""
File: main.py
Heiner Alcala-Salas
Final Project: Budget Tracker
"""
from BudgetTracker import BudgetTracker
from Category import Category
from breezypythongui.breezypythongui import EasyFrame
from tkinter import StringVar, OptionMenu
from tkinter import PhotoImage
#import matplotlib.pyplot as plt


class BudgetTrackerGUI(EasyFrame):
    def __init__(self):
        """Initialize the GUI and the budget tracker."""
        EasyFrame.__init__(self, title="Budget Tracker")

        # Initialize the BudgetTracker instance
        self.tracker = BudgetTracker()
        #app heading logo, imports image
        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   columnspan = 2,
                                   sticky = "NSEW")
        self.image = PhotoImage(file = "dollar_icon.gif")
        imageLabel["image"] = self.image

        # Add Income Section
        # Add a label, button and input field for income
        self.addLabel(text = "Income:",
                      row = 1, column = 0)
        self.incomeField = self.addFloatField(value = 0.0,
                                              row = 1,
                                              column = 1)
        self.addButton(text = "Add Income",
                       row = 2, column = 1,
                       command = self.addIncome)

        #add Expense section
        # add a dropdown for selecting a category
        self.addLabel(text = "Category:",
                      row = 3, column = 0)
        self.categoryVar = StringVar()
        self.updateCategoriesDropdown()
        
        # add a label and field for manual category entry
        self.addLabel(text="New Category (Optional):",
                      row = 4, column = 0)
        self.manualCategoryField = self.addTextField(text = "",
                                                     row = 4,
                                                     column = 1)
        
        # add a button to add expense
        self.addLabel(text = "Expense:",
                      row = 6, column = 0)
        self.expenseField = self.addFloatField(value = 0.0,
                                               row = 6,
                                               column = 1)
        self.addButton(text="Add Expense",
                       row = 7, column = 1,
                       command = self.addExpense)

        # add buttons for category management
        self.addLabel(text = "Add/Remove Category:",
                      row = 8, column = 0)
        self.editCategoryField = self.addTextField(text = "",
                                                  row = 8,
                                                  column = 1)
        self.addButton(text = "Add Category",
                       row = 9, column = 0,
                       command = self.addCategory)
        self.addButton(text="Remove Category",
                       row = 9, column = 1,
                       command = self.removeCategory)
        # adda a label to see account details a button to view balance
        # adda a button to list categories
        self.addLabel(text = "Account Details:",
                      row = 11, column = 0)
        self.addButton(text = "View Balance",
                       row = 12, column = 0,
                       command = self.viewBalance)
        self.addButton(text = "List Categories",
                       row = 12, column = 1,
                       command = self.listCategories)
        # adds a button to display the chart
        self.addButton(text="View Chart",
                       row = 13, column = 0,
                       command = self.showChart)

         # exit button
        self.addButton(text = "Exit",
                       row = 13,
                       column = 1,
                       command = self.exitApplication)

    def updateCategoriesDropdown(self):
        """Populate the category dropdown menu with available categories."""
        # creates a list of categories, starting with the default "Select Category" option
        categories = ["Select Category"] + list(self.tracker.categories.keys())
        self.categoryVar.set("Select Category")  # Reset to default

        # create the dropdown menu and place it on the grid
        dropdown = OptionMenu(self, self.categoryVar, *categories)
        dropdown.grid(row = 3,
                      column = 1,
                      sticky = "EW")

    def addIncome(self):
        """Handle adding income."""
        try:
            amount = self.incomeField.getNumber()       # retrieves income amount input
            if amount > 0:                                  #validates amount to be greater than 0
                message = self.tracker.add_income(amount)   # add income and display confirmation message
                self.messageBox(title = "Success",
                                message = message)
            else:                                           #else display invalidate message
                self.messageBox(title = "Error",
                                message = "Income must be greater than 0.")
        except ValueError:                      # catches non numeri values
            self.messageBox(title = "Error",
                            message = "Please enter a valid income amount.")

    def addExpense(self):
        """Handle adding an expense to a category or a new manual category."""
        try:
            amount = self.expenseField.getNumber()              # gets expense amount input
            dropdown_category = self.categoryVar.get()          # gets category value from dropdown menu
            manual_category = self.manualCategoryField.getText().strip()    # gets manual category input

            if amount <= 0:                 #Validates expense to be greater than 0, if not returns message
                self.messageBox(title = "Error",
                                message = "Expense must be greater than 0.")
                return

            if dropdown_category == "Select Category" and manual_category:      #if drop down menu is default and manual inputis not applys manual input
                # add the manual category and then the expense
                self.tracker.add_category(manual_category)          # adds manual category input to file
                self.updateCategoriesDropdown()                     # calls methos to update the dropdown menu values
                message = self.tracker.add_expense(amount, manual_category) #adds exoenses along with category
                self.messageBox(title = "Success",      #confirmation message
                                message = message)
            elif dropdown_category != "Select Category":    #if drop down category is selected, value ot default
                # use the selected dropdown category
                message = self.tracker.add_expense(amount, dropdown_category)   #adds category selected along with expenses
                self.messageBox(title = "Success",      #confirmation message
                                message = message)
            else:
                # error if neither a valid dropdown nor manual category is provided
                self.messageBox(title = "Error",
                                message = "Please select or enter a valid category.")
        except ValueError:          # catches non numeric values entered at expenses field
            self.messageBox(title = "Error",
                            message = "Please enter a valid expense amount.")

    def addCategory(self):
        """Handle adding a new category."""
        name = self.editCategoryField.getText().strip()     # gets category value from new/remove category field
        
        if name:
            message = self.tracker.add_category(name)   #validates and adds category, displays confirmation message   
            self.messageBox(title = "Success",
                            message = message)      
            self.updateCategoriesDropdown()  # updates the dropdown menu
        else:
            self.messageBox(title = "Error",        # displays error message if category field is empty
                            message = "Category name cannot be empty.")

    def removeCategory(self):
        """Handle removing a category."""
        category_name = self.editCategoryField.getText().strip()        #gets category name from input field
        if category_name == "Select Category":          # checks if default category is selected, displays error message if is
            self.messageBox(title = "Error",
                            message = "Please select a valid category to remove.")
        else:
            message = self.tracker.remove_category(category_name)       #removes category and displays confirmation message
            self.messageBox(title = "Success",
                            message = message)
            self.updateCategoriesDropdown()  # Updates the dropdown menu

    def viewBalance(self):
        """Display the total income, remaining balance, and total expenses."""
        total_balance = self.tracker.get_total_balance()        # gets total balance and stores it in variable
        message = (                                             # displays account summary
            "Total Income: $" + "%.2f" % total_balance['income'] + "\n" +
            "Remaining Balance: $" + "%.2f" % total_balance['remaining_balance'] + "\n" +
            "Total Expenses: $" + "%.2f" % total_balance['total_expenses']
        )
        self.messageBox(title = "Balance",          # message box with title and stored message
                        message = message)

    def listCategories(self):
        """Display the list of categories and their total expenses."""
        categories_list = self.tracker.list_categories()    # retrieves categories from file
        if categories_list == "No categories to display":   # if there are no categories store
            self.messageBox(title = "Categories",
                            message = categories_list)
        else:   
            self.messageBox(title = "Categories",           # else displays category list
                            message = categories_list)

    def showChart(self):
        """Generate a chart comparing total income to total expenses."""
        # Import matplotlib.pyplot dynamically to avoid slow booting time
        import matplotlib.pyplot as plt
        # get income and total expenses
        total_balance = self.tracker.get_total_balance()
        total_income = total_balance['income']
        total_expenses = total_balance['total_expenses']
        remaining_balance = total_balance['remaining_balance']

        # data for the chart, categories and respective values
        categories = ['Income', 'Expenses', 'Remaining Balance']
        values = [total_income, total_expenses, remaining_balance]

        # Create the bar chart with specifit size and colors for each category
        plt.figure(figsize=(8, 5)) # sets chart size
        plt.bar(categories, values, color=['green', 'red', 'blue']) #creates bars for each catefory
        plt.title('Income vs Expenses Comparison') #chart title
        plt.ylabel('Amount ($)') #labels for y axis
        plt.xlabel('Category')  #labels for x axis

        for i, v in enumerate(values):
            plt.text(i, v + 50, "$" + "%.2f" % v, ha='center', va='bottom')

        # Display the chart
        plt.tight_layout()
        plt.show()


    def exitApplication(self):
        """Exit the application."""
        self.messageBox(title = "Exit",
                        message = "Goodbye! See you soon.")
        self.destroy()  # Close the GUI window
                                                                          

def main():
    BudgetTrackerGUI().mainloop()

    
if __name__ == "__main__":
    main()

