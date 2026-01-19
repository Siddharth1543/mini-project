# Expense Tracker Project

# list of all expenses in form of dictionary
expensesList = []
print("Welcome to Expense Tracker")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    
    choice = int(input("Please Enter Your Choice : "))
   
# Add Expense
    if (choice == 1):
        date = input("Enter the date of expense : ")
        category = input("Enter the category(food,travel,etc.) : ")
        description = input("Enter description of expense : ")
        amount = float(input("Enter the amount : "))
        
        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        
        expensesList.append(expense)
        print(" \n Expense is added successfully")
        
# View All Expenses
    elif (choice == 2):
        if (len(expensesList) == 0):
            print("No expenses added.")
        else:
            print("====These are your expenses====")
            count = 1
            for eachexp in expensesList:
                print(f"Expense no. {count} -> {eachexp['date']}, {eachexp['category']}, {eachexp['description']},{eachexp['amount']}")
                count += 1

# 3. View Total expense
    elif (choice == 3):
        total = 0
        for eachexp in expensesList:
            total = total + eachexp["amount"]
            
        print("\n Total Expense = ",total)
        
        
# 4. EXIT
    elif (choice == 4):
        print("Thankyou for using our system")
        break
    
    else:
        print("Invalid Choice")
