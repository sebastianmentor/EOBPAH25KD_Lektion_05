from accounts import Account, Transaction, TransactionType, datetime
import json

ACCOUNTS_FILE = "accounts.json"
DATETIME_FORMAT = "%d/%m/%Y, %H:%M:%S"

class ATM:
    def __init__(self, accounts:dict[int,Account] = None):
        self._accounts = accounts or {}
        self._current_account = None


    def create_account(self, account_number:int):
        if account_number in self._accounts: raise ValueError("Account allready exist!")
        self._accounts[account_number] = Account(account_number)

    def _get_accounts(self) -> dict[int,Account]:
        return self._accounts

    def _accounts_to_json(self):
        accounts = []
        for acc_nr, acc in self._accounts.items():
            acc_dict = {"acc_id":acc_nr,
                        "balance":acc.balance,
                        "created":acc.created.strftime(DATETIME_FORMAT),
                        "transactions":[]}
            for trans in acc.get_transactions():
                trans_dict = {"amount":trans.amount,
                              "date":trans.date.strftime(DATETIME_FORMAT),
                              "type":trans.type.value
                            }
                acc_dict["transactions"].append(trans_dict)

            accounts.append(acc_dict)

        return accounts


    @classmethod
    def load_accounts(cls) -> dict[int,Account]:
        # logic to load accounts from file!
        with open(ACCOUNTS_FILE, "r") as f:
            accounts = json.load(f)

        acc_dict = {}
        for acc in accounts:
            trans = []
            for t in acc["transactions"]:
                trans.append(Transaction(
                    t["amount"],
                    datetime.strptime(t["date"],DATETIME_FORMAT),
                    TransactionType(t["type"])
                ))
            
            acc_dict[acc["acc_id"]] = Account(
                acc["acc_id"],
                acc["balance"],
                datetime.strptime(acc["created"],DATETIME_FORMAT),
                trans
            )

        return acc_dict
    
    @classmethod
    def save_accounts(cls, atm:ATM) -> None:
        # logic to save accounts
        with open(ACCOUNTS_FILE, "w") as f:
            json.dump(atm._accounts_to_json(), f, indent=2)

if __name__ == "__main__":
    atm = ATM(ATM.load_accounts())
    # atm = ATM()
    atm.create_account(82828)
    atm.create_account(10010)
    ATM.save_accounts(atm)