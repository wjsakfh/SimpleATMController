from typing import Dict, List

class BankAPI:
    def __init__(self):
        self.accounts = {
            '1234567890': {'pin': '1234', 'balance': 1000},
            '0987654321': {'pin': '4321', 'balance': 1},
        }

    def verify_pin(self, card_number: str, pin: str) -> bool:
        return self.accounts.get(card_number, {}).get('pin') == pin

    def get_balance(self, card_number: str) -> int:
        return self.accounts.get(card_number, {}).get('balance', 0)

    def deposit(self, card_number: str, amount: int) -> bool:
        if card_number in self.accounts:
            self.accounts[card_number]['balance'] += amount
            return True
        return False

    def withdraw(self, card_number: str, amount: int) -> bool:
        if card_number in self.accounts and self.accounts[card_number]['balance'] >= amount:
            self.accounts[card_number]['balance'] -= amount
            return True
        return False