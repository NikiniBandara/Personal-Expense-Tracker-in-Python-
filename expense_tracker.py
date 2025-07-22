import csv
from datetime import datetime

##add expense
def add_expenses():
    print("Add new expense\n")

    #date
    while True:
        date_in = input("enter date (YYYY-MM-DD):").strip() #remove leading/tailing whitespaces
        try:
            parsed = datetime.strptime(date_in, "%Y-%m-%d")
            if parsed.date() > datetime.now().date():
                print("Warning! future date\n")
            date = date_in
            break #exit loop if date is valid
        except ValueError:
            print("invalid. use YYYY-MM-DD\n")
            continue

    #amount
    while True:
        try:
            amount = float(input("Enter amount:").strip())
            if amount <= 0:
                print("Amount must be positive\n")
                continue
            break
        except ValueError:
            print("Invalid. try again\n")

    #category
    while True:
        category = input("Enter category (eg. Food, Transport, Bill\n): ")
        if category == "": #if empty
            print("can't be empty\n")
            continue
        break
        #if not category:
            #category = "Uncategorized"

    #adding
    expense = [date, amount, category]
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)

    print("Expense added :)")



def disp_menu():
    print("Expense Tracker\n")
    print("1. Add Expense\n")
    print("2. View All Expenses\n")
    print("3. View Expenses by Category\n")
    print("4. Show Monthly Summary\n")
    print("5. Exit prog\n")

def main():
    while True:
        disp_menu()
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_expenses()
        elif choice == "2":
            View_all_ex()
        elif choice == "3":
            View_by_category()
        elif choice == "4":
            Monthly_sum()
        elif choice == "5":
            print("Exiting")
            break
        else:
            print("Invalid. try again\n")

if __name__ == "__main__":
    main()
