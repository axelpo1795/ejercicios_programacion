import unittest
from io import StringIO
import sys
from E5_s6 import count_cap_low


class TestCountCapLow(unittest.TestCase):
    
    # Capturar la salida de print antes de cada test
    def setUp(self):
        self.captured_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_output
    # Restaurar la salida estándar después de cada test
    def tearDown(self):
        sys.stdout = self.original_stdout
    # Funciona con texto que tiene mayúsculas y minúsculas
    def test_text_with_caps_and_lowercase(self):
        try:
            count_cap_low("I love Nación Sushi")
            output = self.captured_output.getvalue()
            self.assertIn("2 upper cases", output)
            self.assertIn("12 lower cases", output)
            print("[PASSED] test_text_with_caps_and_lowercase")
        except Exception:
            print("[FAILED] test_text_with_caps_and_lowercase")
            raise
    # Funciona con solo letras mayúsculas
    def test_only_uppercase(self):
        try:
            count_cap_low("HELLO")
            output = self.captured_output.getvalue()
            self.assertIn("5 upper cases", output)
            self.assertIn("0 lower cases", output)
            print("[PASSED] test_only_uppercase")
        except Exception:
            print("[FAILED] test_only_uppercase")
            raise
    # Funciona con solo letras minúsculas
    def test_only_lowercase(self):
        try:
            count_cap_low("hello")
            output = self.captured_output.getvalue()
            self.assertIn("0 upper cases", output)
            self.assertIn("5 lower cases", output)
            print("[PASSED] test_only_lowercase")
        except Exception:
            print("[FAILED] test_only_lowercase")
            raise
    # Funciona con cadena vacía
    def test_empty_string(self):
        try:
            count_cap_low("")
            output = self.captured_output.getvalue()
            self.assertIn("0 upper cases", output)
            self.assertIn("0 lower cases", output)
            print("[PASSED] test_empty_string")
        except Exception:
            print("[FAILED] test_empty_string")
            raise
    # No funciona con parámetros que no sean string (int)
    def test_invalid_parameter_integer(self):
        with self.assertRaises((TypeError, AttributeError)):
            count_cap_low(12345)
        print("[PASSED] test_invalid_parameter_integer")
    # No funciona con parámetros que no sean string (None)
    def test_invalid_parameter_none(self):
        with self.assertRaises((TypeError, AttributeError)):
            count_cap_low(None)
        print("[PASSED] test_invalid_parameter_none")


if __name__ == '__main__':
    unittest.main()
