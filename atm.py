from typing import Optional
from datetime import datetime

class Withdraw:
    ...

class Deposit:
    ...

class Transaction:
    def __init__(self, amount:float, type:Withdraw|Deposit, date:datetime):
        self._amount = amount
        self._type = type
        self._date = date

    def get_amount(self) -> float:
        return self._amount
    
    def get_type(self) -> Withdraw|Deposit:
        return self._type
    
    def get_date(self) -> datetime:
        return self._date
    
    def __str__(self) -> str:
        return f"Amount: {self._amount}\n" \
               f"Type: {'withdraw' if isinstance(self._type, Withdraw) else 'deposit'}\n" \
               f"Date: {self._date.strftime("%Y-%m-%d %H:%M:%S")}\n"

class Account:
    def __init__(
            self, 
            acc_number:int, 
            saldo:float, 
            transactions:Optional[list[Transaction]] = None
            ):
        
        self._account_number:int = acc_number
        self._saldo:float = saldo
        self._transactions:list[Transaction] = transactions or []

    def get_saldo(self) -> float:
        return self._saldo
    
    def get_account_number(self) -> int:
        return self._account_number
    
    def get_transactions(self) -> list[Transaction]:
        return self._transactions.copy()
    
    def deposit(self, amount:float) -> None:
        if amount <= 0: 
            raise ValueError(f"Invalid deposit! Amount {amount} must be positive!")
        
        new_transaction = Transaction(amount, Deposit(), datetime.now())
        self._transactions.append(new_transaction)

        self._saldo += amount


    def withdraw(self, amount:float) -> bool:
        if amount <= 0:
            raise ValueError(f"Invalid withdraw! Amount {amount} must be positive!")
        
        if amount > self._saldo:
            return False
        
        new_transaction = Transaction(amount, Withdraw(), datetime.now())
        self._transactions.append(new_transaction)

        self._saldo -= amount
        return True
    
def get_amount_from_user() -> Optional[float]:
    try:
        amount = float(input("Enter amount: "))
        return amount
    except ValueError:
        print("Invalid amount!")
        return None

def account_menue(account:Account) -> None:
    while True:
        print("1. Show saldo")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Transactions")
        print("0. Go back")

        choice = input("Enter choice")

        if choice == "0": 
            break

        elif choice == "1":
            print(account.get_saldo())

        elif choice == "2":
            amount = get_amount_from_user()
            
            if not amount: continue

            try:
                account.deposit(amount)
                print("Deposit success!")
            except ValueError as e:
                print(e)


        elif choice == "3":
            amount = get_amount_from_user()
            
            if not amount: continue
            
            try:
                success_witdraw = account.withdraw(amount)
                
                print("Withdraw success!") if success_witdraw else print("Insufficient founds!")

            except ValueError as e:
                print(e)

        elif choice == "4":
            print(f"Transactions for {account.get_account_number()}")
            for transaction in account.get_transactions():
                print(transaction)

        else:
            print("Invalid choice")
        


def log_in(accounts:list[Account], account_number:int) -> Account|None:
    for account in accounts:
        if account.get_account_number() == account_number:
            return account
        
    return None
    
def run_atm():
    accounts:list[Account] = [Account(1, 0), Account(2, 0), Account(3, 0)]

    
    while True:
        print("1. Create Account")
        print("2. Log in")
        print("0. Shut down")

        choice = input("Enter choice")

        if choice == "0": 
            break

        elif choice == "1":
            try:
                new_account_number = int(input("Enter new account number: "))
            except ValueError:
                print("Invalid number!")

            if new_account_number <= 0:
                print("Account number must be positive!")

            elif log_in(accounts, new_account_number):
                print(f"Account with {new_account_number} already exist! Log in instead...")

            else:
                accounts.append(Account(new_account_number, 0))
                print(f"Account {new_account_number} created!")

        elif choice == "2":
            
            account_number = input("Enter Account number: ")

            if not account_number.isdigit():
                print("Must be a positive number!")

            account = log_in(accounts, int(account_number))
            if account:
                account_menue(account)
            else:
                print("Account does not exist!")

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    run_atm()