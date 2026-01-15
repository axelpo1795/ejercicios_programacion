import os
from actions import add_students, show_students, show_top_3, show_average_of_averages
from data import export_to_csv, import_from_csv

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def print_menu(students):
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

def run(students):
    while True:
        try:
            choice = print_menu(students)

            if choice == "1":
                add_students(students)
                input("\nPresione Enter para continuar...")
                clear()
            elif choice == "2":
                show_students(students)
                input("\nPresione Enter para continuar...")
                clear()
            elif choice == "3":
                show_top_3(students)
                input("\nPresione Enter para continuar...")
                clear()
            elif choice == "4":
                show_average_of_averages(students)
                input("\nPresione Enter para continuar...")
                clear()
            elif choice == "5":
                filename = "students.csv"
                export_to_csv(filename, students)
                input("\nPresione Enter para continuar...")
                clear()
            elif choice == "6":
                filename = "students.csv"
                imported = import_from_csv(filename)
                if imported is None:
                    input("\nPresione Enter para continuar...")
                    clear()
                else:
                    students.extend(imported)
                    print(f"Se importaron {len(imported)} estudiantes.")
                    input("\nPresione Enter para continuar...")
                    clear()
            elif choice == "7":
                print("Saliendo del programa...")
                break
            else:
                raise ValueError("Opción no válida. Ingrese una opción del 1 al 7.")
        except ValueError as e:
            clear()
            print(str(e))
