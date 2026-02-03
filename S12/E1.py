from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self,balance = 0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("El depósito debe ser positivo.")
        return False
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
class SavingsAccount(BankAccount):

    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def deposit(self, amount):
        return super().deposit(amount)
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Monto de retiro inválido.")
            return False
        if self.balance - amount < self.min_balance:
            raise ValueError("El retiro haría que el balance quede debajo del mínimo requerido.")
        self.balance -= amount
        return True
