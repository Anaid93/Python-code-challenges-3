'''Create a program that simulates the operation of 
a bank account. The program should ask the user 
whether he/she wants to make a deposit or a 
withdrawal until the user decides to terminate the program.'''

balance  = 0
incomes =[]
withdrawals=[]
while True:
    print("What do you want to do?")
    print("1- Income")
    print("2- Withdrawal")
    option = int(input("Choose one option (any other to finish): "))    
    
    if option == 1:
        income = int(input("Enter the amount: "))
        balance += income   
        incomes.append(income)
        print("Your final balance is:", balance)     
        
    elif option == 2:
        withdrawal = int(input("Enter the amount: "))
        
        if balance < withdrawal:
            print("Sorry, there is not enough balance.")
        else:
            balance -= withdrawal
            withdrawals.append(withdrawal)
            print("Your final balance is:", balance)   
    else:
        print("Incomes:", incomes)
        print("Withdrawals:", withdrawals)
        break


