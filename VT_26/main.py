from atm import ATM

def main(atm:ATM):
    # atm.create_account(6666)
    ...



if __name__ == "__main__":
    atm = ATM(ATM.load_accounts())
    main(atm)
    ATM.save_accounts(atm)