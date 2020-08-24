from unittest import TestCase, main
from numbers import Number
from pdb import set_trace


def validate_cache(func, cache={}):
    # TODO: Criar closure
    def validate_apply_cache(self, x, y=None):
        key = False

        if y == None:
            y = cache['value']
            key = True

        if isinstance(x, Number) and isinstance(y, Number):
            if key:
                cache['value'] = func(self, y, x)
            else:
                cache['value'] = func(self, x, y)
            return cache['value']
        else:
            raise Exception('Insira somente números.')
    return validate_apply_cache


class Calc:
    @validate_cache
    def soma(self, x, y):
        return x + y

    @validate_cache
    def mul(self, x, y):
        return x * y

    @validate_cache
    def sub(self, x, y):
        return x - y
    
    @validate_cache
    def div(self, x, y):
        return x / y


class Testes_calculadora(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 2), 4)

    def test_soma_neg(self):
        self.assertEqual(self.calc.soma(-2, -3), -5)

    def test_soma_float(self):
        self.assertEqual(self.calc.soma(2.0, 1.0), 3.0)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 2), 0)

    def test_sub_float(self):
        self.assertEqual(self.calc.sub(2.0, 2.0), 0)

    def test_soma_string(self):
        with self.assertRaises(Exception):
            (self.calc.soma('yuuki', 'asuna'))

    def test_sub_string(self):
        with self.assertRaises(Exception):
            (self.calc.sub('yuuki', 'asuna'))
    
    def test_mul(self):
        self.assertEqual(self.calc.mul(3, 3), 9)

    def test_mul_string(self):
        with self.assertRaises(Exception):
            self.calc.mul(3, 'yuuki')

    def test_div(self):
        self.assertEqual(self.calc.div(3, 3), 1)

    def test_div_string(self):
        with self.assertRaises(Exception):
            self.calc.div(3, 'asuna')

    def test_cache_soma(self):
        self.assertEqual(self.calc.soma(self.calc.soma(2, 2)), 8)

    def test_cache_sub(self):
        """
        Na primeira subtração 10 - 5 o resultado é 5

        cache - resultado == 0
        """
        self.assertEqual(self.calc.sub(self.calc.sub(10, 5)), 0)

    def test_sub_com_result_neg_mul_cache(self):
        self.assertEqual(self.calc.sub(3, 10), -7)
        self.assertEqual(self.calc.mul(3), -21)

    def test_sub_com_result_neg_soma_cache(self):
        self.assertEqual(self.calc.sub(3, 10), -7)
        self.assertEqual(self.calc.soma(3), -4)

    def test_soma_com_result_pos_com_sub_cache(self):
        self.assertEqual(self.calc.soma(1, 1), 2)
        self.assertEqual(self.calc.sub(3), -1)

if __name__ == "__main__":
    main()
