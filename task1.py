class BudgetCategory:
    def __init__(self, name: str, budget: float):
    
        self._name = name
        self._budget = budget
        self._expenses = 0.0

    @property
    def name(self) -> str:

        return self._name

    @property
    def budget(self) -> float:

        return self._budget

    @property
    def expenses(self) -> float:
        
        return self._expenses

    @property
    def remaining_budget(self) -> float:
    
        return self._budget - self._expenses

    @budget.setter
    def budget(self, new_budget: float):
        
        if new_budget >= 0:
            self._budget = new_budget
        else:
            raise ValueError

    @name.setter
    def name(self, new_name: str):


        if new_name.strip():  
            self._name = new_name
        else:
            raise ValueError

    def add_expense(self, amount: float):


        if amount <= 0:
            raise ValueError
        if amount > self.remaining_budget:
            raise ValueError

        self._expenses += amount

    def __str__(self) -> str:
        
        return (
            f"Category: {self._name}\n"
            f"Allocated Budget: ${self._budget:.2f}\n"
            f"Expenses: ${self._expenses:.2f}\n"
            f"Remaining Budget: ${self.remaining_budget:.2f}"
        )


grocery_category = BudgetCategory("Groceries", 250.00)
grocery_category.add_expense(50.00)
grocery_category.add_expense(75.50)

print(grocery_category)