import unittest
from E6_s6 import order_words


class TestOrderWords(unittest.TestCase):
    
    # Ordena palabras separadas por guiones correctamente
    def test_basic_ordering(self):
        try:
            result = order_words("python-variable-funcion-computadora-monitor")
            expected = "computadora-funcion-monitor-python-variable"
            self.assertEqual(result, expected)
            print("[PASSED] test_basic_ordering")
        except Exception:
            print("[FAILED] test_basic_ordering")
            raise
    # Cadena ya ordenada permanece igual
    def test_already_sorted(self):
        try:
            result = order_words("a-b-c")
            expected = "a-b-c"
            self.assertEqual(result, expected)
            print("[PASSED] test_already_sorted")
        except Exception:
            print("[FAILED] test_already_sorted")
            raise
    # Una sola palabra sin guiones
    def test_single_word(self):
        try:
            result = order_words("hello")
            expected = "hello"
            self.assertEqual(result, expected)
            print("[PASSED] test_single_word")
        except Exception:
            print("[FAILED] test_single_word")
            raise
    # Cadena vacía
    def test_empty_string(self):
        try:
            result = order_words("")
            expected = ""
            self.assertEqual(result, expected)
            print("[PASSED] test_empty_string")
        except Exception:
            print("[FAILED] test_empty_string")
            raise

if __name__ == '__main__':
    unittest.main()