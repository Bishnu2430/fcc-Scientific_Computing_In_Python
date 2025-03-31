'''
# Description:  
This program is a simple expense tracker designed to help users manage their personal finances. It allows users to record, view, and analyze their expenses in an organized way.

#What It Does:  
1. Add Expenses: Users can input the amount spent and the category (e.g., food, transport, entertainment) for each expense.  
2. List All Expenses: Displays a list of all recorded expenses, showing the amount and category for each entry.  
3. Show Total Expenses: Calculates and displays the total amount of all recorded expenses.  
4. Filter by Category: Filters and lists expenses belonging to a specific category.  
5. Exit: Ends the program when the user is done.  

The program uses a menu-based interface, making it easy for users to interact and keep track of their spending.
'''

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()