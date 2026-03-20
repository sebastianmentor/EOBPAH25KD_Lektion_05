from datetime import datetime
from enum import Enum
from typing import Optional

class TransactionType(Enum):
    WITDRAW = 1
    DEPOSIT = 2
    TRANSFER = 3

class Transaction:
    def __init__(self,
                 amount:int,
                 transaction_date:datetime,
                 transaction_type:TransactionType
                 ):
        self._amount = amount
        self._date = transaction_date
        self._type = transaction_type

    @property
    def amount(self) -> int:
        return self._amount
    
    @property
    def date(self) -> datetime:
        return self._date
    
    @property
    def type(self) -> TransactionType:
        return self._type
        
class InsuficientAmountError(Exception):
    ...

class Account:
    def __init__(self, 
                acc_nr:int,
                balance:int = 0,
                crated:datetime = None,
                transactions:Optional[list[Transaction]] = None):
        
        self._acc_nr = acc_nr
        self._balance = balance
        self._created = crated or datetime.now()
        self._transations =transactions or []

    @property
    def balance(self) -> int:
        return self._balance

    @property
    def account_number(self) -> int:
        return self._acc_nr
    
    @property
    def created(self) -> datetime:
        return self._created
    
    def get_transactions(self) -> list[Transaction]:
        return self._transations.copy()
    
    def deposit(self, amount:int) -> None:
        if amount < 0: raise ValueError("Cant deposit negative money!!")

        self._transations.append(Transaction(amount, datetime.now(), TransactionType.DEPOSIT))
        self._balance += amount

    def withdraw(self, amount:int) -> None:
        if amount < 0: raise ValueError("Cant deposit negative money!!")
        if amount > self.balance: raise InsuficientAmountError("Not enough money!")

        self._transations.append(Transaction(amount, datetime.now(), TransactionType.WITDRAW))
        self._balance -= amount        
