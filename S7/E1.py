def get_number(message):
    """Ask the user for a number and validate that it is truly numeric."""
    while True:
        user_input = input(message)
        try:
            # Aqui validamos que realmente sea número
            number = float(user_input)
            return number
        except ValueError:
            print("Error: debe ingresar un número válido, no caracteres.")

def get_menu_option():
    """Ask the user for a menu option and validate."""
    while True:
        option = input("Opción: ")
        try:
            option_int = int(option)
            if 1 <= option_int <= 6:
                return option_int
            else:
                print("Error: opción fuera de rango (1-6).")
        except ValueError:
            print("Error: debe ingresar un número del menú, no letras.")

def sum_numbers(base_number, add_number):
    current = base_number + add_number
    return current

def substract(base_number, add_number):
    current = base_number - add_number
    return current

def multiply(base_number, add_number):
    current = base_number * add_number
    return current

def divide(base_number, add_number):
    current = base_number / add_number
    return current

def calculator():
    current = 0.0
    print("**********Calculadora Lyft**********\nNúmero actual:", current)

    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Borrar resultado (volver a cero)")
        print("6. Salir")

        option = get_menu_option()

        if option == 6:
            print("Saliendo...")
            break

        if option == 5:
            current = 0.0
            print("Resultado borrado. Número actual:", current)
            continue

        # Para 1–4, pedir un número nuevo
        new_number = get_number("Ingrese el número: ")

        try:
            if option == 1:
                current = sum_numbers(current, new_number)
            elif option == 2:
                current = substract(current,new_number)
            elif option == 3:
                current = multiply(current,new_number)
            elif option == 4:
                if new_number == 0:
                    raise ZeroDivisionError("Intento de dividir entre cero.")
                current = divide(current,new_number)
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
            continue

        print("Número actual:", current)

calculator()
