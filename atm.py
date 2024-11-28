from typing import Dict, List
from bank_api import BankAPI

class ATM:
    def __init__(self, bank_api: BankAPI):
        self.bank_api = bank_api
        self.current_card = None

    def insert_card(self, card_number: str) -> bool:
        if card_number in self.bank_api.accounts:
            self.current_card = card_number
            return True
        return False

    def enter_pin(self, pin: str) -> bool:
        if self.current_card:
            return self.bank_api.verify_pin(self.current_card, pin)
        return False

    def select_account(self) -> bool:
        return self.current_card is not None

    def check_balance(self) -> int:
        if self.current_card:
            return self.bank_api.get_balance(self.current_card)
        return 0

    def deposit(self, amount: int) -> bool:
        if self.current_card:
            return self.bank_api.deposit(self.current_card, amount)
        return False

    def withdraw(self, amount: int) -> bool:
        if self.current_card:
            return self.bank_api.withdraw(self.current_card, amount)
        return False

    def end_session(self):
        self.current_card = None