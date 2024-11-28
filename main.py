from bank_api import BankAPI
from atm import ATM

# ---- user input & user information ---- #
CARDNUM = '1234567890'
PIN = '1234'
DEPOSIT_AMOUNT = 500
WITHDRAW_AMOUNT = 200
LARGE_WITHDRAW_AMOUNT = 10000

def main():
    print("# ---- transaction starts ---- #")
    bank_api = BankAPI()
    atm = ATM(bank_api)

    print(f"\nInserting card: {CARDNUM}")
    if atm.insert_card(CARDNUM):
        print("Card accepted.")
        
        print(f"\nEntering PIN: {PIN}")
        if atm.enter_pin(PIN):
            print("PIN accepted.")
            
            if atm.select_account():
                print("Account selected.")
                
                # Check balance
                balance = atm.check_balance()
                print(f"\nCurrent balance: ${balance}")
                
                # Deposit money
                if atm.deposit(DEPOSIT_AMOUNT):
                    print(f"Deposited ${DEPOSIT_AMOUNT}")
                    print(f"New balance: ${atm.check_balance()}")
                
                # Withdraw money
                if atm.withdraw(WITHDRAW_AMOUNT):
                    print(f"\nWithdrew ${WITHDRAW_AMOUNT}")
                    print(f"New balance: ${atm.check_balance()}")
                else:
                    print(f"Failed to withdraw ${WITHDRAW_AMOUNT}")
                
                # Try to withdraw more than the balance
                if atm.withdraw(LARGE_WITHDRAW_AMOUNT):
                    print(f"\nWithdrew ${LARGE_WITHDRAW_AMOUNT}")
                else:
                    print(f"\nFailed to withdraw ${LARGE_WITHDRAW_AMOUNT} - Insufficient funds")
                
                print(f"Final balance: ${atm.check_balance()}")
            else:
                print("Failed to select account.")
        else:
            print("Incorrect PIN.")
    else:
        print("Card not recognized.")

    atm.end_session()
    print("\n# ---- ATM session ended ---- #")

if __name__ == "__main__":
    main()
