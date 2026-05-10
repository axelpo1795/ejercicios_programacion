"""Main GUI window for the finance application."""

import PySimpleGUI as sg
from data_handler import DataHandler
from forms import AddCategoryForm, AddExpenseForm, AddIncomeForm


class MainWindow:
    """Main GUI window for the finance application."""
    
    def __init__(self):
        """Initialize the main window."""
        self.data_handler = DataHandler()
        sg.theme('DarkBlue3')
        self.window = None
    
    def _create_layout(self):
        """Create the main window layout."""
        # Button section
        button_section = [
            [
                sg.Button('Agregar Categoría', key='-ADD_CAT-', size=(15, 1)),
                sg.Button('Agregar Gasto', key='-ADD_EXP-', size=(15, 1)),
                sg.Button('Agregar Ingreso', key='-ADD_INC-', size=(15, 1))
            ]
        ]
        
        # Transactions table
        headers = ['Detalle', 'Categoría', 'Monto', 'Tipo', 'Fecha']
        transactions_data = self._get_transactions_table_data()
        
        table_section = [
            [sg.Table(
                transactions_data,
                headings=headers,
                display_row_numbers=True,
                auto_size_columns=False,
                col_widths=[20, 15, 12, 10, 12],
                key='-TABLE-',
                size=(70, 15)
            )]
        ]
        
        # Total section
        total = self.data_handler.get_total()
        total_color = 'green' if total >= 0 else 'red'
        
        total_section = [
            [sg.Text(f"Saldo Total: ₡{total:.2f}", 
                     text_color=total_color, 
                     font=('Arial', 12, 'bold'),
                     key='-TOTAL-')]
        ]
        
        # Complete layout
        layout = [
            [sg.Text('Gestor de Finanzas', font=('Arial', 16, 'bold'))],
            [sg.Column(button_section, expand_x=True)],
            [sg.Text('Transacciones:', font=('Arial', 10, 'bold'))],
            [sg.Column(table_section, expand_x=True, expand_y=True)],
            [sg.Column(total_section, expand_x=True)],
            [sg.Button('Actualizar', key='-REFRESH-'), 
             sg.Button('Eliminar Seleccionado', key='-DELETE-'),
             sg.Button('Salir', key='-EXIT-')]
        ]
        
        return layout
    
    def _get_transactions_table_data(self):
        """Get transaction data formatted for the table."""
        transactions = self.data_handler.get_all_transactions()
        data = []
        for transaction in transactions:
            sign = '+' if transaction.transaction_type == 'ingreso' else '-'
            amount_display = f"{sign}{transaction.amount:.2f}"
            type_display = 'Ingreso' if transaction.transaction_type == 'ingreso' else 'Gasto'
            data.append([transaction.detail, transaction.category, amount_display, type_display, transaction.date])
        return data if data else [['Sin transacciones aún', '', '', '', '']]
    
    def _refresh_display(self):
        """Refresh the table and total display."""
        try:
            self.data_handler.load_data()
            transactions_data = self._get_transactions_table_data()
            self.window['-TABLE-'].update(transactions_data)
            
            total = self.data_handler.get_total()
            total_color = 'green' if total >= 0 else 'red'
            self.window['-TOTAL-'].update(
                f"Saldo Total: ₡{total:.2f}",
                text_color=total_color
            )
        except Exception as e:
            sg.popup(f"Error al actualizar pantalla: {str(e)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
    
    def _add_category(self):
        """Handle add category button."""
        try:
            categories = self.data_handler.get_categories_names()
            new_category = AddCategoryForm.show(categories)
            
            if new_category:
                self.data_handler.add_category(new_category)
                sg.popup(f"¡La categoría '{new_category}' se creó exitosamente!", title='Éxito', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'green'))
                self._refresh_display()
        except ValueError as e:
            sg.popup(f"Error: {str(e)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
        except Exception as e:
            sg.popup(f"Error inesperado: {str(e)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
    
    def _add_expense(self):
        """Handle add expense button."""
        try:
            categories = self.data_handler.get_categories_names()
            form = AddExpenseForm(categories)
            result = form.show()
            
            if result:
                detail, category, amount = result
                self.data_handler.add_transaction(detail, category, amount, 'gasto')
                sg.popup("¡Gasto agregado exitosamente!", title='Éxito', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'green'))
                self._refresh_display()
        except ValueError as e:
            sg.popup(f"Error: {str(e)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
        except Exception as e:
            sg.popup(f"Error inesperado: {str(e)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
    
    def _add_income(self):
        """Handle add income button."""
        try:
            categories = self.data_handler.get_categories_names()
            form = AddIncomeForm(categories)
            result = form.show()
            
            if result:
                detail, category, amount = result
                self.data_handler.add_transaction(detail, category, amount, 'ingreso')
                sg.popup("¡Ingreso agregado exitosamente!", title='Éxito', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'green'))
                self._refresh_display()
        except ValueError as exception:
            sg.popup(f"Error: {str(exception)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
        except Exception as exception:
            sg.popup(f"Error inesperado: {str(exception)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
    
    def _delete_selected(self):
        """Handle delete selected transaction."""
        if not self.window['-TABLE-'].get():
            sg.popup("Ninguna transacción seleccionada.", title='Advertencia', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'orange'))
            return
        
        try:
            selected_row = self.window['-TABLE-'].get()[0]
            transactions = self.data_handler.get_all_transactions()
            
            if selected_row < len(transactions):
                transaction_to_delete = transactions[selected_row]
                self.data_handler.delete_transaction(transaction_to_delete.transaction_id)
                sg.popup("¡Transacción eliminada exitosamente!", title='Éxito', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'green'))
                self._refresh_display()
            else:
                sg.popup("Selección inválida.", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
        except Exception as e:
            sg.popup(f"Error al eliminar transacción: {str(e)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))
    
    def run(self):
        """Run the main window."""
        layout = self._create_layout()
        self.window = sg.Window('Gestor de Finanzas', layout, finalize=True, size=(900, 600))
        
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED or event == '-EXIT-':
                break
            elif event == '-ADD_CAT-':
                self._add_category()
            elif event == '-ADD_EXP-':
                self._add_expense()
            elif event == '-ADD_INC-':
                self._add_income()
            elif event == '-REFRESH-':
                self._refresh_display()
            elif event == '-DELETE-':
                self._delete_selected()
        
        self.window.close()


def main():
    """Entry point for the application."""
    try:
        app = MainWindow()
        app.run()
    except Exception as e:
        sg.popup(f"Error fatal: {str(e)}", title='Error', button_type=sg.POPUP_BUTTONS_OK, button_color=('white', 'red'))


if __name__ == '__main__':
    main()
