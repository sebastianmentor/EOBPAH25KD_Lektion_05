# class Customer:
#     customer_id = [0]


# c1 = Customer()
# c2 = Customer()

# print(id(c1.customer_id))
# c1.customer_id[0] = 1
# print(id(c1.customer_id))
# print(id(c2.customer_id))

# print(c1.customer_id)
# print(c2.customer_id)

# class Customer:
#     def __init__(self,customer_id:int) -> None:
#         self.__id = customer_id

#     def get_id(self) -> int:
#         return self.__id
    

# c1 = Customer(1001)
# print(c1.get_id())

# print(c1._Customer__id)
# c1.__id = 1234
# print(c1.__id)
# print(c1._Customer__id)
# print(c1.__dict__)

# print(c1.get_id())


# class Customer:
#     id = 88
#     def __init__(self,customer_id:int) -> None:
#         self.id = customer_id

#     @property
#     def id(self) -> int:
#         return self._id
    
#     @id.setter
#     def id(self, new_id:int) -> None:
#         if new_id < 1: raise ValueError("Id cant be negative")

#         self._id = new_id
    

# c1 = Customer(5555)
# print(c1.id)
# c1.id = 1234
# print(c1.id)
# print(Customer.id)
# print(c1.__dict__)

from enum import Enum, auto
from datetime import datetime

class Bill:
    def __init__(self, amount:int, due_date:datetime) -> None:
        self._amount = amount
        self._due_date = due_date

    @property
    def amount(self) -> int:
        return self._amount
    
    @property
    def due_date(self) -> datetime:
        return self._due_date
    
    def __str__(self) -> str:
        return f"Amount to pay is {self.amount} and is due to {self.due_date.strftime("%d/%m/%Y")}"

class CustomerType(Enum):
    REGULAR = auto()
    VIP = auto()

class Customer:
    def __init__(self,
                 customer_id:int, 
                 customer_type:CustomerType,
                 bills:list[Bill] = None,
                 ) -> None:
        
        self.id = customer_id
        self.type = customer_type
        self._bills = bills or []

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, new_id:int) -> None:
        if new_id < 1: raise ValueError("Id cant be negative")

        self._id = new_id

    def get_bills(self) -> list[Bill]:
        return self._bills.copy()
    
    def append_new_bill(self, new_bill:Bill) -> None:
        self._bills.append(new_bill)


def customer_has_vip(customer:Customer) -> bool:
    return True if customer.type == CustomerType.VIP else False

c1 = Customer(9999, CustomerType.REGULAR)
print(customer_has_vip(c1))

c2 = Customer(9999, CustomerType.VIP)
print(customer_has_vip(c2))

c2.append_new_bill(Bill(15, datetime.now()))
c2.append_new_bill(Bill(50, datetime(2026, 4, 1)))

print(c1.get_bills())

for bill in c2.get_bills():
    print(bill)
