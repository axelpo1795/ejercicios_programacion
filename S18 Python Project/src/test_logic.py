"""
Unit tests for the Finance Manager application.
Tests core business logic and data operations.
"""

import unittest
import os
import json
from models import Transaction, Category
from data_handler import DataHandler


class TestCategory(unittest.TestCase):
    """Test cases for Category model."""
    
    def test_category_creation(self):
        """Test creating a category."""
        category = Category("Comida")
        self.assertEqual(category.name, "Comida")
        self.assertIsNotNone(category.category_id)
    
    def test_category_to_dict(self):
        """Test converting category to dictionary."""
        category = Category("Transporte", "cat_001")
        category_dict = category.to_dict()
        self.assertEqual(category_dict['name'], "Transporte")
        self.assertEqual(category_dict['category_id'], "cat_001")
    
    def test_category_from_dict(self):
        """Test creating category from dictionary."""
        data = {'name': 'Salud', 'category_id': 'cat_002'}
        category = Category.from_dict(data)
        self.assertEqual(category.name, 'Salud')
        self.assertEqual(category.category_id, 'cat_002')


class TestTransaction(unittest.TestCase):
    """Test cases for Transaction model."""
    
    def test_transaction_creation_ingreso(self):
        """Test creating an income transaction."""
        transaction = Transaction(
            detail="Pago de trabajo",
            category="Salario",
            amount=1000.00,
            transaction_type="ingreso"
        )
        self.assertEqual(transaction.detail, "Pago de trabajo")
        self.assertEqual(transaction.category, "Salario")
        self.assertEqual(transaction.amount, 1000.00)
        self.assertEqual(transaction.transaction_type, "ingreso")
    
    def test_transaction_creation_gasto(self):
        """Test creating an expense transaction."""
        transaction = Transaction(
            detail="Compra en supermercado",
            category="Comida",
            amount=50.00,
            transaction_type="gasto"
        )
        self.assertEqual(transaction.detail, "Compra en supermercado")
        self.assertEqual(transaction.category, "Comida")
        self.assertEqual(transaction.amount, 50.00)
        self.assertEqual(transaction.transaction_type, "gasto")
    
    def test_transaction_to_dict(self):
        """Test converting transaction to dictionary."""
        transaction = Transaction("Taxi", "Transporte", 15.00, "gasto")
        transaction_dict = transaction.to_dict()
        self.assertEqual(transaction_dict['detail'], "Taxi")
        self.assertEqual(transaction_dict['category'], "Transporte")
        self.assertEqual(transaction_dict['amount'], 15.00)
        self.assertEqual(transaction_dict['transaction_type'], "gasto")
    
    def test_transaction_from_dict(self):
        """Test creating transaction from dictionary."""
        data = {
            'detail': 'Pago de servicios',
            'category': 'Utilidades',
            'amount': 100.00,
            'transaction_type': 'gasto',
            'date': '2026-05-04',
            'transaction_id': 'trans_001'
        }
        transaction = Transaction.from_dict(data)
        self.assertEqual(transaction.detail, 'Pago de servicios')
        self.assertEqual(transaction.category, 'Utilidades')
        self.assertEqual(transaction.amount, 100.00)


class TestDataHandler(unittest.TestCase):
    """Test cases for DataHandler class."""
    
    def setUp(self):
        """Set up test fixture with temporary data file."""
        self.test_filename = 'test_finance_data.json'
        self.data_handler = DataHandler(self.test_filename)
    
    def tearDown(self):
        """Clean up test data file."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
    
    def test_add_category(self):
        """Test adding a category."""
        category = self.data_handler.add_category("Alimentos")
        self.assertEqual(category.name, "Alimentos")
        self.assertIn(category, self.data_handler.categories)
    
    def test_add_duplicate_category_raises_error(self):
        """Test that adding duplicate category raises ValueError."""
        self.data_handler.add_category("Categoría")
        with self.assertRaises(ValueError):
            self.data_handler.add_category("Categoría")
    
    def test_add_transaction_gasto(self):
        """Test adding an expense transaction."""
        self.data_handler.add_category("Comida")
        transaction = self.data_handler.add_transaction(
            detail="Almuerzo",
            category="Comida",
            amount=30.00,
            transaction_type="gasto"
        )
        self.assertEqual(transaction.detail, "Almuerzo")
        self.assertIn(transaction, self.data_handler.transactions)
    
    def test_add_transaction_ingreso(self):
        """Test adding an income transaction."""
        self.data_handler.add_category("Salario")
        transaction = self.data_handler.add_transaction(
            detail="Pago de trabajo",
            category="Salario",
            amount=2000.00,
            transaction_type="ingreso"
        )
        self.assertEqual(transaction.detail, "Pago de trabajo")
        self.assertEqual(transaction.category, "Salario")
        self.assertIn(transaction, self.data_handler.transactions)
    
    def test_add_transaction_without_category_raises_error(self):
        """Test that missing category raises ValueError."""
        with self.assertRaises(ValueError):
            self.data_handler.add_transaction(
                detail="Compra",
                category=None,
                amount=50.00,
                transaction_type="gasto"
            )
        
        with self.assertRaises(ValueError):
            self.data_handler.add_transaction(
                detail="Ingreso",
                category=None,
                amount=100.00,
                transaction_type="ingreso"
            )
    
    def test_get_total_income(self):
        """Test calculating total income."""
        self.data_handler.add_category("Salario")
        self.data_handler.add_transaction("Trabajo", "Salario", 1000.00, "ingreso")
        self.data_handler.add_transaction("Bonificación", "Salario", 500.00, "ingreso")
        total_income = self.data_handler.get_total_income()
        self.assertEqual(total_income, 1500.00)
    
    def test_get_total_expenses(self):
        """Test calculating total expenses."""
        self.data_handler.add_category("Comida")
        self.data_handler.add_transaction("Desayuno", "Comida", 20.00, "gasto")
        self.data_handler.add_transaction("Almuerzo", "Comida", 30.00, "gasto")
        total_expenses = self.data_handler.get_total_expenses()
        self.assertEqual(total_expenses, 50.00)
    
    def test_get_total_balance(self):
        """Test calculating total balance (ingreso - gasto)."""
        self.data_handler.add_category("Salario")
        self.data_handler.add_category("Comida")
        self.data_handler.add_transaction("Salario", "Salario", 2000.00, "ingreso")
        self.data_handler.add_transaction("Compra", "Comida", 500.00, "gasto")
        total_balance = self.data_handler.get_total()
        self.assertEqual(total_balance, 1500.00)
    
    def test_delete_transaction(self):
        """Test deleting a transaction."""
        self.data_handler.add_category("Salario")
        transaction = self.data_handler.add_transaction(
            "Compra",
            "Salario",
            100.00,
            "ingreso"
        )
        initial_count = len(self.data_handler.transactions)
        self.data_handler.delete_transaction(transaction.transaction_id)
        final_count = len(self.data_handler.transactions)
        self.assertEqual(initial_count - 1, final_count)
    
    def test_get_categories_names(self):
        """Test getting list of category names."""
        self.data_handler.add_category("Transporte")
        self.data_handler.add_category("Diversión")
        category_names = self.data_handler.get_categories_names()
        self.assertIn("Transporte", category_names)
        self.assertIn("Diversión", category_names)
    
    def test_invalid_amount_raises_error(self):
        """Test that invalid amount raises ValueError."""
        self.data_handler.add_category("Salario")
        with self.assertRaises(ValueError):
            self.data_handler.add_transaction("Test", "Salario", 0, "ingreso")
        
        with self.assertRaises(ValueError):
            self.data_handler.add_transaction("Test", "Salario", -100, "ingreso")
    
    def test_empty_detail_raises_error(self):
        """Test that empty detail raises ValueError."""
        self.data_handler.add_category("Salario")
        with self.assertRaises(ValueError):
            self.data_handler.add_transaction("", "Salario", 100.00, "ingreso")
    
    def test_save_and_load_data(self):
        """Test saving and loading data persistence."""
        self.data_handler.add_category("Prueba")
        self.data_handler.add_transaction("Ingreso", "Prueba", 100.00, "ingreso")
        
        # Load data again from file
        new_handler = DataHandler(self.test_filename)
        self.assertEqual(len(new_handler.categories), 1)
        self.assertEqual(len(new_handler.transactions), 1)
        self.assertEqual(new_handler.categories[0].name, "Prueba")


if __name__ == '__main__':
    unittest.main()
