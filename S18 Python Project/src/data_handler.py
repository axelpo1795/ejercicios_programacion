"""
Data handler for persisting and loading financial data.
"""

import json
import os
from typing import List
from models import Transaction, Category


class DataHandler:
    """Handles saving and loading of financial data to/from JSON files."""
    
    def __init__(self, filename: str = 'finance_data.json'):
        """
        Initialize the data handler.
        
        Args:
            filename: Name of the file to store data
        """
        self.filename = filename
        self.transactions: List[Transaction] = []
        self.categories: List[Category] = []
        self.load_data()
    
    def load_data(self):
        """Load transactions and categories from file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as data_file:
                    data = json.load(data_file)
                    
                    # Migrate old transaction types to new ones
                    transactions_data = data.get('transactions', [])
                    for transaction_data in transactions_data:
                        if transaction_data.get('transaction_type') == 'income':
                            transaction_data['transaction_type'] = 'ingreso'
                        elif transaction_data.get('transaction_type') == 'expense':
                            transaction_data['transaction_type'] = 'gasto'
                    
                    self.transactions = [
                        Transaction.from_dict(transaction_data) for transaction_data in transactions_data
                    ]
                    self.categories = [
                        Category.from_dict(category) for category in data.get('categories', [])
                    ]
                    
                    # Save migrated data
                    self.save_data()
            else:
                self.transactions = []
                self.categories = []
        except json.JSONDecodeError:
            raise ValueError(f"Error leyendo {self.filename}. El archivo puede estar corrupto.")
        except Exception as e:
            raise ValueError(f"Error al cargar datos: {str(e)}")
    
    def save_data(self):
        """Save transactions and categories to file."""
        try:
            data = {
                'transactions': [transaction.to_dict() for transaction in self.transactions],
                'categories': [category.to_dict() for category in self.categories]
            }
            with open(self.filename, 'w') as data_file:
                json.dump(data, data_file, indent=4)
        except Exception as e:
            raise ValueError(f"Error al guardar datos: {str(e)}")
    
    def add_category(self, category_name: str) -> Category:
        """
        Add a new category.
        
        Args:
            category_name: Name of the category
            
        Returns:
            The newly created category
        """
        # Check if category already exists
        if any(category.name.lower() == category_name.lower() for category in self.categories):
            raise ValueError(f"La categoría '{category_name}' ya existe.")
        
        category = Category(category_name)
        self.categories.append(category)
        self.save_data()
        return category
    
    def add_transaction(self, detail: str, category: str, amount: float, 
                       transaction_type: str) -> Transaction:
        """
        Add a new transaction.
        
        Args:
            detail: Transaction description
            category: Category name
            amount: Transaction amount
            transaction_type: 'ingreso' or 'gasto'
            
        Returns:
            The newly created transaction
        """
        if not amount or amount <= 0:
            raise ValueError("El monto debe ser un número positivo.")
        
        if not detail:
            raise ValueError("El detalle no puede estar vacío.")
        
        # Both ingreso and gasto transactions require a category
        if not category:
            raise ValueError("Se debe seleccionar una categoría.")
        
        # Validate category exists
        if not any(cat.name == category for cat in self.categories):
            raise ValueError(f"La categoría '{category}' no existe.")
        
        transaction = Transaction(detail, category, amount, transaction_type)
        self.transactions.append(transaction)
        self.save_data()
        return transaction
    
    def delete_transaction(self, transaction_id: str):
        """Delete a transaction by ID."""
        self.transactions = [transaction for transaction in self.transactions if transaction.transaction_id != transaction_id]
        self.save_data()
    
    def get_categories_names(self) -> List[str]:
        """Get all category names."""
        return [category.name for category in self.categories]
    
    def get_all_transactions(self) -> List[Transaction]:
        """Get all transactions."""
        return sorted(self.transactions, key=lambda t: t.date, reverse=True)
    
    def get_total_income(self) -> float:
        """Calculate total income (ingreso)."""
        try:
            return sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == 'ingreso')
        except Exception as e:
            raise ValueError(f"Error al calcular ingresos: {str(e)}")
    
    def get_total_expenses(self) -> float:
        """Calculate total expenses (gasto)."""
        try:
            return sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == 'gasto')
        except Exception as e:
            raise ValueError(f"Error al calcular gastos: {str(e)}")
    
    def get_total(self) -> float:
        """Calculate the total balance (ingreso - gasto)."""
        try:
            return self.get_total_income() - self.get_total_expenses()
        except Exception as e:
            raise ValueError(f"Error al calcular el total: {str(e)}")
