"""
Data models for the finance application.
"""

from datetime import datetime
from typing import Optional


class Category:
    """Represents a transaction category."""
    
    def __init__(self, name: str, category_id: Optional[str] = None):
        """
        Initialize a category.
        
        Args:
            name: Category name
            category_id: Unique identifier for the category
        """
        self.name = name
        self.category_id = category_id or str(hash(name))
    
    def to_dict(self):
        """Convert category to dictionary."""
        return {
            'name': self.name,
            'category_id': self.category_id
        }
    
    @staticmethod
    def from_dict(data: dict):
        """Create a category from a dictionary."""
        return Category(data['name'], data.get('category_id'))
    
    def __repr__(self):
        return f"Category(name='{self.name}')"


class Transaction:
    """Represents a financial transaction (income or expense)."""
    
    def __init__(self, detail: str, category: str, amount: float, 
                 transaction_type: str, date: Optional[str] = None,
                 transaction_id: Optional[str] = None):
        """
        Initialize a transaction.
        
        Args:
            detail: Description of the transaction
            category: Category name
            amount: Transaction amount (positive value)
            transaction_type: 'ingreso' or 'gasto'
            date: Transaction date (defaults to today)
            transaction_id: Unique identifier for the transaction
        """
        self.detail = detail
        self.category = category
        self.amount = float(amount)
        self.transaction_type = transaction_type
        self.date = date or datetime.now().strftime('%Y-%m-%d')
        self.transaction_id = transaction_id or str(hash(f"{detail}{category}{amount}{self.date}"))
    
    def to_dict(self):
        """Convert transaction to dictionary."""
        return {
            'detail': self.detail,
            'category': self.category,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'date': self.date,
            'transaction_id': self.transaction_id
        }
    
    @staticmethod
    def from_dict(data: dict):
        """Create a transaction from a dictionary."""
        return Transaction(
            data['detail'],
            data['category'],
            data['amount'],
            data['transaction_type'],
            data.get('date'),
            data.get('transaction_id')
        )
    
    def __repr__(self):
        sign = '+' if self.transaction_type == 'ingreso' else '-'
        return f"Transaction(detail='{self.detail}', category='{self.category}', amount={sign}{self.amount})"
