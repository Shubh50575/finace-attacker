import os
import datetime
DATA_FILE="my_finance.txt"

def add_transaction():
    print("\n ADD TRANSACTION")
    while True:
        transation_type =input("+ Income or - Expense? (i/e): ").lower()
        if transation_type in ("i","e"):
            break
        print("Please enter 'i','e' ")

    amount = input("Enter the amount : $")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    symbol = "+" if transation_type == "i" else "-"

    with open(DATA_FILE,"a") as file:
        file.write(f"{today}|{symbol}{amount}|{category}|{description}\n")
        print("Transation added sucessfully!")
        
def view_transaction():
    if not os.path.exists(DATA_FILE):
        print("No Transaction Found")
        return
    print("\n TRANSACTIONS")
    print("-" * 60)
    print("DATE   AMOUNT   CATEGORY   DESCRIPTION")
    print("-" * 60)
    with open(DATA_FILE,"r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts)<4:
                # print(f"Skipping invalid line: {line.strip()}")
                continue
            date = parts[0]
            amount = parts[1]
            category = parts[2]
            description = parts[3]
            emoji = "💰" if amount.startswith('+') else "💰"


            print(f"{date}   {emoji} {amount}   {category}   {description}")
    
def get_summary():
    if not os.path.exists(DATA_FILE):
        print("\n No Transaction Found")
        return
    total_income=0
    total_expense=0

    with open(DATA_FILE,"r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts)<2:
                # print(f"Skipping invalid line :{line}")
                continue
            amount = parts[1]
            if amount.startswith("+"):
                total_income += float(amount[1:])
            else:
                total_expense += float(amount[1:])

    balance = total_income - total_expense

    print("\n FINANCIAL SUMMARY")
    print(f"Total Income: ${total_income:.2f}") 
    print(f"Total Expense: ${total_expense:.2f}") 
    print(f"Balance: ${balance:.2f}") 
def main():
    while True:
        print("\n" + "=" * 30)
        print("💸 FINANCE TRACKER 💸")
        print("="*30)
        print("1. Add Transaction")
        print("2. View Transaction")
        print("3. Summary")
        print("4. Exit")
        choice = input("\n Choice(1-4):").strip()
        if choice =="1":
            add_transaction()
        elif choice =="2":
            view_transaction()
        elif choice =="3":
            get_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please Go with 1 to 4")


    
main()
