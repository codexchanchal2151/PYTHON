balance = 0.0

while True:
    print("\n--- BANK MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        print(f"Current Balance: Rs. {balance:.2f}")
    elif choice == "2":
        amount = float(input("Enter deposit amount: Rs. "))
        if amount > 0:
            balance += amount
            print(f"Deposited: Rs. {amount:.2f}")
        else:
            print("Invalid amount!")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: Rs. "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Withdrawn: Rs. {amount:.2f}")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            print("Invalid amount!")
    elif choice == "4":
        print("Thank you for using our banking service!")
        break
    else:
        print("Invalid choice, please select between 1 and 4.")
