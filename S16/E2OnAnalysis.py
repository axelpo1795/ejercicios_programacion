# E1
def print_numbers_times_2(numbers_list):
    	for number in numbers_list:
		print(number * 2)
# O(n) porque se recorre la lista una vez, y el tiempo de ejecución crece linealmente con el tamaño de la lista

# E2
def check_if_lists_have_an_equal(list_a, list_b):
    	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False
# O(n^2) porque en el peor de los casos, se comparan todos los elementos de ambas listas

# E3
def print_10_or_less_elements(list_to_print):
    	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])
# O(1) porque el número de elementos a imprimir es constante (10 o menos), independientemente del tamaño de la lista
		
# E4
def generate_list_trios(list_a, list_b, list_c):
    	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 
# O(n^3) porque en el peor de los casos, se generan trios con todos los elementos de las tres listas (n * n * n)