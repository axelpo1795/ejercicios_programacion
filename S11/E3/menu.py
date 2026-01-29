import os
from actions import add_students, show_students, show_top_3, show_average_of_averages
from data import DataManager


class Menu:
    """Gestiona la interfaz de menú de la aplicación."""
    
    def __init__(self, manager):
        self.manager = manager
        self.data_manager = DataManager()
        self.clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        """Muestra el menú principal y retorna la opción seleccionada."""
        print("===================================")
        print("Bienvenido al sistema de gestión de estudiantes.\n")
        print("===================================\n")
        print("Menu principal:")
        print("1. Agregar estudiantes")
        print("2. Mostrar estudiantes")
        print("3. Top 3 estudiantes por promedio")
        print("4. Promedio general de promedios")
        print("5. Exportar datos a CSV")
        print("6. Importar datos desde CSV")
        print("7. Salir del programa")
        choice = input("Seleccione una opción: ")
        print("===================================\n")
        return choice
    
    def handle_option(self, choice):
        """Procesa la opción seleccionada por el usuario."""
        if choice == "1":
            add_students(self.manager)
            input("\nPresione Enter para continuar...")
            self.clear()
        elif choice == "2":
            show_students(self.manager)
            input("\nPresione Enter para continuar...")
            self.clear()
        elif choice == "3":
            show_top_3(self.manager)
            input("\nPresione Enter para continuar...")
            self.clear()
        elif choice == "4":
            show_average_of_averages(self.manager)
            input("\nPresione Enter para continuar...")
            self.clear()
        elif choice == "5":
            filename = "students.csv"
            self.data_manager.export_to_csv(filename, self.manager)
            input("\nPresione Enter para continuar...")
            self.clear()
        elif choice == "6":
            filename = "students.csv"
            imported_students = self.data_manager.import_from_csv(filename)
            if imported_students is None:
                input("\nPresione Enter para continuar...")
                self.clear()
            else:
                self.manager.extend(imported_students)
                print(f"Se importaron {len(imported_students)} estudiantes.")
                input("\nPresione Enter para continuar...")
                self.clear()
        elif choice == "7":
            print("Saliendo del programa...")
            return False
        else:
            raise ValueError("Opción no válida. Ingrese una opción del 1 al 7.")
        
        return True
    
    def run(self):
        """Inicia el bucle principal de la aplicación."""
        while True:
            try:
                choice = self.display_menu()
                if not self.handle_option(choice):
                    break
            except ValueError as e:
                self.clear()
                print(str(e))
