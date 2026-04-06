import unittest
from E7_s6 import get_prime_nums


class TestGetPrimeNums(unittest.TestCase):
    
    # Lista con números primos y no primos
    def test_mixed_list(self):
        try:
            result = get_prime_nums([1, 4, 6, 7, 13, 9, 67])
            expected = [7, 13, 67]
            self.assertEqual(result, expected)
            print("[PASSED] test_mixed_list")
        except Exception:
            print("[FAILED] test_mixed_list")
            raise
    # Lista vacía
    def test_empty_list(self):
        try:
            result = get_prime_nums([])
            expected = []
            self.assertEqual(result, expected)
            print("[PASSED] test_empty_list")
        except Exception:
            print("[FAILED] test_empty_list")
            raise
    # Lista con solo números primos
    def test_all_primes(self):
        try:
            result = get_prime_nums([2, 3, 5, 7, 11])
            expected = [2, 3, 5, 7, 11]
            self.assertEqual(result, expected)
            print("[PASSED] test_all_primes")
        except Exception:
            print("[FAILED] test_all_primes")
            raise
    # Lista sin números primos
    def test_no_primes(self):
        try:
            result = get_prime_nums([1, 4, 6, 8, 9, 10])
            expected = []
            self.assertEqual(result, expected)
            print("[PASSED] test_no_primes")
        except Exception:
            print("[FAILED] test_no_primes")
            raise
    # Lista con números negativos
    def test_with_negatives(self):
        try:
            result = get_prime_nums([-1, 0, 1, 2, 3])
            expected = [2, 3]
            self.assertEqual(result, expected)
            print("[PASSED] test_with_negatives")
        except Exception:
            print("[FAILED] test_with_negatives")
            raise
    # Lista con un solo número primo
    def test_single_prime(self):
        try:
            result = get_prime_nums([7])
            expected = [7]
            self.assertEqual(result, expected)
            print("[PASSED] test_single_prime")
        except Exception:
            print("[FAILED] test_single_prime")
            raise


if __name__ == '__main__':
    unittest.main()