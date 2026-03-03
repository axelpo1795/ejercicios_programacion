def bubble_sort(list_numbers):
    numbers_in_list = len(list_numbers)
    
    # Recorre la lista numbers_in_list veces
    for current_pass in range(numbers_in_list):
        # Bandera para optimizar: si no hay cambios, ya está ordenada
        has_swapped = False
        
        # Compara elementos adyacentes
        for current_position in range(0, numbers_in_list - current_pass - 1):
            if list_numbers[current_position] > list_numbers[current_position + 1]:
                # Intercambia si están en orden incorrecto
                list_numbers[current_position], list_numbers[current_position + 1] = list_numbers[current_position + 1], list_numbers[current_position]
                has_swapped = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not has_swapped:
            break
    
    return list_numbers


# Ejemplo de uso
if __name__ == "__main__":
    # Lista desordenada
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", numbers)
    
    # Ordena la lista
    sorted_list = bubble_sort(numbers)
    print("Lista ordenada:", sorted_list)
