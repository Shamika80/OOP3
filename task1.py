class BudgetCategory:
    # ... (Your existing code remains the same) ...

    def display_details(self):
        """Displays the details of the budget category."""
        print("Category Name:", self.__category_name)
        print("Allocated Budget: ${:.2f}".format(self.__allocated_budget))
        print("Total Expenses: ${:.2f}".format(self._get_expenses()))
        print("Expenses:")  # Added to display individual expenses
        for expense in self.__expenses:
            print("- ${:.2f}".format(expense))  # Display each expense

    def add_expense(self, amount):
        """Adds an expense to the budget category."""
        self.__expenses.append(amount)  # Add expense to the list
        self.__allocated_budget -= amount  # Reduce allocated budget by expense

    # ... (Rest of your getter, setter, add_expense, display_details methods) ...

    def _get_expenses(self):
        return self.__original_budget - self.__allocated_budget 

# Create a budget category (Correct way)
grocery_budget = BudgetCategory("Groceries", 200)

# Add some expenses
grocery_budget.add_expense(55)
grocery_budget.add_expense(30)

# Display the category details
grocery_budget.display_details()