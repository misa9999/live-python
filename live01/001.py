from unittest import TestCase, main

from abc2 import eh_par

# TDD TEST DRIVE IN DEVELOPE


class Testes(TestCase):
    def test_par(self):
        self.assertEqual(eh_par(2), True)

    def test_impar(self):
        self.assertEqual(eh_par(3), False)

    def test_string(self):
        self.assertEqual(eh_par(''), False)

    def test_float(self):
        self.assertEqual(eh_par(4.4), False)


if __name__ == "__main__":
    main()
