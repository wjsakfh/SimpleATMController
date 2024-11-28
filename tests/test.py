import sys
import os
sys.path.append("./")
from bank_api import BankAPI
from atm import ATM

def test_atm():
    print("# ---- test starts ---- #")
    bank_api = BankAPI()
    atm = ATM(bank_api)

    # TC 1: Successful transaction
    print("# ---- TC 1: Successful transaction passed ---- #")

    assert atm.insert_card('1234567890')
    assert atm.enter_pin('1234')
    assert atm.select_account()
    assert atm.check_balance() == 1000
    assert atm.deposit(500)
    assert atm.check_balance() == 1500
    assert atm.withdraw(200)
    assert atm.check_balance() == 1300
    atm.end_session()

    # TC 2: Incorrect PIN
    print("# ---- TC 2: Incorrect PIN passed ---- #")

    assert atm.insert_card('0987654321')
    assert not atm.enter_pin('1111')
    atm.end_session()

    # TC 3: Insufficient funds
    print("# ---- TC 3: Insufficient funds passed ---- #")
    assert atm.insert_card('0987654321')
    assert atm.enter_pin('4321')
    assert atm.select_account()
    assert not atm.withdraw(3000)
    atm.end_session()

    print("# ---- All tests done ---- #")

if __name__ == "__main__":
    test_atm()