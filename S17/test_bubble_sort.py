import unittest
from BubbleSort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    
    # Funciona con una lista pequeña
    def test_small_list(self):
        try:
            list_numbers = [64, 34, 25, 12, 22, 11, 90]
            expected = [11, 12, 22, 25, 34, 64, 90]
            result = bubble_sort(list_numbers.copy())
            self.assertEqual(result, expected)
            print("[PASSED] test_small_list")
        except Exception:
            print("[FAILED] test_small_list")
            raise
    # Funciona con una lista grande (más de 100 elementos)
    def test_large_list(self):
        try:
            # Crea una lista de 150 números aleatorios
            list_numbers = list(range(150, 0, -1))  # Lista en orden descendente del 150 al 1
            expected = list(range(1, 151))  # Lista en orden ascendente del 1 al 150
            result = bubble_sort(list_numbers)
            self.assertEqual(result, expected)
            print("[PASSED] test_large_list")
        except Exception:
            print("[FAILED] test_large_list")
            raise
    # Funciona con una lista vacía
    def test_empty_list(self):
        try:
            list_numbers = []
            expected = []
            result = bubble_sort(list_numbers)
            self.assertEqual(result, expected)
            print("[PASSED] test_empty_list")
        except Exception:
            print("[FAILED] test_empty_list")
            raise
    # No funciona con parámetros que no sean una lista (string)
    def test_string_parameter(self):
        try:
            with self.assertRaises(TypeError):
                bubble_sort("string")
            print("[PASSED] test_string_parameter")
        except Exception:
            print("[FAILED] test_string_parameter")
            raise
    # No funciona con parámetros que no sean una lista (int)
    def test_integer_parameter(self):
        try:
            with self.assertRaises(TypeError):
                bubble_sort(123)
            print("[PASSED] test_integer_parameter")
        except Exception:
            print("[FAILED] test_integer_parameter")
            raise
    # No funciona con parámetros que no sean una lista (None)
    def test_none_parameter(self):
        try:
            with self.assertRaises(TypeError):
                bubble_sort(None)
            print("[PASSED] test_none_parameter")
        except Exception:
            print("[FAILED] test_none_parameter")
            raise
    # Funciona con una lista de un solo elemento
    def test_single_element(self):
        try:
            list_numbers = [42]
            expected = [42]
            result = bubble_sort(list_numbers.copy())
            self.assertEqual(result, expected)
            print("[PASSED] test_single_element")
        except Exception:
            print("[FAILED] test_single_element")
            raise
    # Funciona con lista que contiene elementos duplicados
    def test_list_with_duplicates(self):
        try:
            list_numbers = [5, 2, 8, 2, 9, 1, 5, 5]
            expected = [1, 2, 2, 5, 5, 5, 8, 9]
            result = bubble_sort(list_numbers.copy())
            self.assertEqual(result, expected)
            print("[PASSED] test_list_with_duplicates")
        except Exception:
            print("[FAILED] test_list_with_duplicates")
            raise
    # Lista ya ordenada
    def test_already_sorted_list(self):
        try:
            list_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
            expected = [1, 2, 3, 4, 5, 6, 7, 8]
            result = bubble_sort(list_numbers.copy())
            self.assertEqual(result, expected)
            print("[PASSED] test_already_sorted_list")
        except Exception:
            print("[FAILED] test_already_sorted_list")
            raise


if __name__ == '__main__':
    unittest.main()
