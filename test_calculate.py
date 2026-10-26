import unittest
from calculate import balls


class PurchasingChecks(unittest.TestCase):
    def test_worked_example(self):
        self.assertEqual(balls('360', '75'), 5)
        self.assertEqual(balls('60', '75'), 1)

    def test_colours_cannot_share_leftovers(self):
        self.assertEqual(sum(balls(n, '75') for n in ['80', '80', '80']), 6)
        self.assertEqual(balls('240', '75'), 4)

    def test_exact_boundary_and_decimal(self):
        self.assertEqual(balls('150', '75'), 2)
        self.assertEqual(balls('0.3', '0.1'), 3)
        self.assertEqual(balls('150.01', '75'), 3)
        self.assertEqual(balls('0', '75'), 0)
        self.assertEqual(balls('75', '75', '1'), 2)

    def test_invalid_inputs(self):
        for values in [('1', '0'), ('-1', '75'), ('NaN', '75'), ('1', 'Infinity'), ('1', '75', '-1')]:
            with self.assertRaises(ValueError):
                balls(*values)


if __name__ == '__main__':
    unittest.main()
