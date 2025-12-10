class Bank:
    def __init__(self):

        self.accounts = []
        self.menu()

    def menu(self):

        while True:
            option = input('''
            \n=== Bank Main Menu ===
            1. Press 1 to Create New Account
            2. Press 2 to Access Account (Login)
            3. Press 3 to Exit
            Enter your choice: ''')
            
            if option == "1":
                self.create_account()
            elif option == "2":
                self.access_account()
            elif option == "3":
                print("Thank you for banking with us. Goodbye!")
                return
            else:
                print("Invalid option. Please try again.")

    def create_account(self):
        print("\n--- Create New Account ---")
        name = input("Enter your name: ")
        

        if any(acc['name'].lower() == name.lower() for acc in self.accounts):
            print("⚠️ An account with this name already exists. Please choose a different name.")
            return

        while True:
            pin = input("Set your 4-digit PIN: ")
            if len(pin) == 4 and pin.isdigit():
                break
            else:
                print("Invalid PIN. PIN must be 4 digits.")

        while True:
            try:
                initial_balance = float(input("Enter initial deposit amount (minimum 0): "))
                if initial_balance >= 0:
                    break
                else:
                    print("Initial deposit cannot be negative.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        

        new_account = {
            'name': name,
            'pin': pin,
            'balance': initial_balance
        }
        
       
        self.accounts.append(new_account)
        print(f"\n✅ Account created successfully for {name}! Initial balance: ${initial_balance:.2f}")

    def access_account(self):
        print("\n--- Account Login ---")
        name = input("Enter your account name: ")
        pin = input("Enter your PIN: ")
        
       
        account = next((acc for acc in self.accounts if acc['name'].lower() == name.lower()), None)
        
        if account and account['pin'] == pin:
            print(f"\n✅ Welcome back, {account['name']}!")
            
            self.account_actions_menu(account)
        else:
            print("❌ Invalid name or PIN.")

    def account_actions_menu(self, account):
        while True:
            option = input(f'''
            \n=== {account['name']}'s Account Menu ===
            1. Press 1 to Check Balance
            2. Press 2 to Deposit Funds
            3. Press 3 to Withdraw Funds
            4. Press 4 to Go Back to Main Menu
            Enter your choice: ''')

            if option == "1":
                self.check_balance(account)
            elif option == "2":
                self.deposit(account)
            elif option == "3":
                self.withdrawal(account)
            elif option == "4":
                print(f"Logging out of {account['name']}'s account.")
                return 
            else:
                print("Invalid option. Please try again.")

    def check_balance(self, account):
        print(f"\n💰 Current Balance for {account['name']}: ${account['balance']:.2f}")

    def deposit(self, account):
        while True:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    account['balance'] += amount
                    print(f"✅ Deposit successful. New Balance: ${account['balance']:.2f}")
                    break
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def withdrawal(self, account):
        
        
        pin_check = input("Re-enter your PIN to authorize withdrawal: ")
        
        if account['pin'] != pin_check:
            print("❌ Wrong PIN. Withdrawal cancelled.")
            return

        while True:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                    continue
                
                if account['balance'] >= amount:
                    account['balance'] -= amount
                    print("✅ Withdrawal successful.")
                    print(f"Remaining Balance: ${account['balance']:.2f}")
                    break
                else:
                    print("❌ Insufficient balance.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")


Bank()