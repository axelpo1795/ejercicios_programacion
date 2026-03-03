def bubble_sort_right_to_left(list_numbers):
    numbers_in_list = len(list_numbers)
    
    # Recorremos desde el final hacia el inicio
    for current_number in range(numbers_in_list - 1, 0, -1):
        # En cada pasada, comparamos elementos de derecha a izquierda
        for number in range(current_number):
            # Si el elemento actual es mayor que el siguiente, intercambiamos
            if list_numbers[number] > list_numbers[number + 1]:
                # Intercambio
                list_numbers[number], list_numbers[number + 1] = list_numbers[number + 1], list_numbers[number]
    
    return list_numbers


if __name__ == "__main__":
    test_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", test_numbers)
    
    result = bubble_sort_right_to_left(test_numbers.copy())
    print("Lista ordenada:", result)
