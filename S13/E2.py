def validate_numbers(func):
    def wrapper(*args, **kwargs):
        # Validar argumentos posicionales
        for i, arg in enumerate(args):
            # Verifica si el argumento no es un número (int o float), o si es un booleano (Bool es un subtipo de int en Python)
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError(
                    f"El parámetro {i} debe ser un número, "
                    f"pero se recibió {type(arg).__name__}: {arg!r}"
                )
        
        # Validar argumentos nombrados
        for key, value in kwargs.items():
            # Verifica si el argumento no es un número (int o float), o si es un booleano (Bool es un subtipo de int en Python)
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(
                    f"El parámetro '{key}' debe ser un número, "
                    f"pero se recibió {type(value).__name__}: {value!r}"
                )
        
        return func(*args, **kwargs)
    return wrapper


@validate_numbers
def sum_numbers(a, b, c):
    return a + b + c

if __name__ == "__main__":
    # Casos válidos
    print("Casos válidos:")
    print(f"sum_numbers(2, 3, 4) = {sum_numbers(2, 3, 4)}")
    print(f"sum_numbers(10, 20, 30) = {sum_numbers(10, 20, 30)}")
    print(f"sum_numbers(2.5, 4.5, 1.5) = {sum_numbers(2.5, 4.5, 1.5)}")
    
    print("\nCasos inválidos:")
    
    # Caso inválido 1: parámetro string
    try:
        print(sum_numbers(2, "3", 4))
    except TypeError as e:
        print(f"Error: {e}")
    
    # Caso inválido 2: parámetro None
    try:
        print(sum_numbers(10, None, 5))
    except TypeError as e:
        print(f"Error: {e}")
    
    # Caso inválido 3: parámetro booleano
    try:
        print(sum_numbers(2, True, 4))
    except TypeError as e:
        print(f"Error: {e}")
