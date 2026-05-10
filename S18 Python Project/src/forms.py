"""Form dialogs for the finance application."""

import PySimpleGUI as sg
from typing import Optional, Tuple


class AddCategoryForm:
    """Dialog form for adding a new category."""
    
    @staticmethod
    def show(categories: list) -> Optional[str]:
        """
        Show the add category dialog.
        
        Args:
            categories: List of existing categories (for validation)
            
        Returns:
            The new category name, or None if cancelled
        """
        layout = [
            [sg.Text('Nombre de Categoría:'), sg.InputText(key='-CATEGORY_NAME-')],
            [sg.Button('Crear'), sg.Button('Cancelar')]
        ]
        
        window = sg.Window('Agregar Categoría', layout)
        
        while True:
            event, values = window.read()
            
            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                window.close()
                return None
            
            if event == 'Crear':
                category_name = values['-CATEGORY_NAME-'].strip()
                
                # Validation
                if not category_name:
                    sg.popup('Por favor ingrese un nombre de categoría.', title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
                    continue
                
                if any(cat.lower() == category_name.lower() for cat in categories):
                    sg.popup(f"La categoría '{category_name}' ya existe.", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
                    continue
                
                window.close()
                return category_name


class AddTransactionForm:
    """Base class for transaction forms (expense/income)."""
    
    def __init__(self, transaction_type: str, categories: list):
        """
        Initialize the form.
        
        Args:
            transaction_type: 'gasto' or 'ingreso'
            categories: List of available categories
        """
        self.transaction_type = transaction_type
        self.categories = categories
    
    def show(self) -> Optional[Tuple[str, str, float]]:
        """
        Show the add transaction dialog.
        
        Returns:
            Tuple of (detail, category, amount) or None if cancelled
        """
        if not self.categories:
            sg.popup(
                'No hay categorías disponibles. Por favor, cree una categoría primero.',
                title='Sin Categorías',
                button_type=sg.POPUP_BUTTONS_OK,
                button_color=('white', 'red')
            )
            return None
        
        title_map = {'gasto': 'Agregar Gasto', 'ingreso': 'Agregar Ingreso'}
        title = title_map.get(self.transaction_type, f'Agregar {self.transaction_type.capitalize()}')
        layout = [
            [sg.Text('Detalle:'), sg.InputText(key='-DETAIL-', size=(30, 1))],
            [sg.Text('Categoría:'), sg.Combo(
                self.categories,
                key='-CATEGORY-',
                readonly=True
            )],
            [sg.Text('Monto:'), sg.InputText(key='-AMOUNT-', size=(15, 1))],
            [sg.Button('Agregar'), sg.Button('Cancelar')]
        ]
        
        window = sg.Window(title, layout)
        
        while True:
            event, values = window.read()
            
            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                window.close()
                return None
            
            if event == 'Agregar':
                detail = values['-DETAIL-'].strip()
                category = values['-CATEGORY-']
                amount_str = values['-AMOUNT-'].strip()
                
                # Validation
                if not detail:
                    sg.popup('Por favor ingrese un detalle/descripción.', title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
                    continue
                
                if not category:
                    sg.popup('Por favor seleccione una categoría.', title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
                    continue
                
                if not amount_str:
                    sg.popup('Por favor ingrese un monto.', title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
                    continue
                
                try:
                    amount = float(amount_str)
                    if amount <= 0:
                        raise ValueError("El monto debe ser mayor que 0.")
                except ValueError as e:
                    sg.popup(f'Monto inválido: {str(e)}', title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
                    continue
                
                window.close()
                return (detail, category, amount)


class AddExpenseForm(AddTransactionForm):
    """Dialog form for adding an expense."""
    
    def __init__(self, categories: list):
        """Initialize the expense form."""
        super().__init__('gasto', categories)


class AddIncomeForm(AddTransactionForm):
    """Dialog form for adding an income."""
    
    def __init__(self, categories: list):
        """Initialize the income form."""
        super().__init__('ingreso', categories)
