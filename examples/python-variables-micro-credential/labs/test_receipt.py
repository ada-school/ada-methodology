"""Unit tests for receipt.py (Atom 5 capstone).

Run:  python3 -m unittest test_receipt.py
"""
import unittest

from receipt import subtotal, apply_tax, build_receipt


class TestReceipt(unittest.TestCase):
    def test_subtotal(self):
        self.assertAlmostEqual(subtotal(2.5, 4), 10.0)

    def test_apply_tax(self):
        self.assertAlmostEqual(apply_tax(100, 0.19), 119.0)

    def test_apply_tax_zero_rate(self):
        self.assertAlmostEqual(apply_tax(50, 0.0), 50.0)

    def test_build_receipt_has_item_and_total(self):
        r = build_receipt("Coffee", 3.0, 2, rate=0.0)
        self.assertIn("Coffee x2", r)
        self.assertIn("TOTAL:    $6.00", r)


if __name__ == "__main__":
    unittest.main()
