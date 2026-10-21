# Expense Tracker Project

expenseslist = [] # List of all Expenses in the form of Dictionary
print("Welcome To Expense Tracker : Kharcha kam kiya karo!")
 
while True:
    print("====Menu====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Enter your Choice :"))


#ADD Expenses 
    if(choice == 1):
        date = input("Enter the Date :")
        category = input("Kis type ka kharcha kiye ? (Food, Travel, Makeup, Books): ")
        description = input("Aur Detail Dedo :")
        amount = float(input("Enter the amount: "))

        expense= {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expenseslist.append(expense)
        print("\n Done Bro. Expense is added Succesfully")

# 2. View All Expense
    elif(choice == 2):
        if(len(expenseslist)==0 ):
            print("No Expenses added. Go and pay some amount! ")

        else:
            print("======This is your all Expenses")
            count = 1
            for eachkharcha in expenseslist:
                print(f"Kharcha Number {count} -> \n {eachkharcha["date"]}, \n {eachkharcha["category"]}, \n {eachkharcha["description"]}, \n {eachkharcha["amount"]}")  
                count = count + 1 

 # 3. View Total Spending                
    elif(choice == 3):
        total = 0
        for eachkharcha in expenseslist: 
            total = total + eachkharcha["amount"]
        
        print("\n Total kharcha = ", total)

# 4. Exit 
    elif(choice == 4):
        print("==== Tysm For using my System ====")
        break

    else:
        print(" INVALID CHOICE! , TRY AGAIN ")