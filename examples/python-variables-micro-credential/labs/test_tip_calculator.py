"""Unit tests for tip_calculator.py (Atom 4).

Run:  python3 -m unittest test_tip_calculator.py
"""
import unittest

from tip_calculator import calculate_tip, grand_total, per_person


class TestTipCalculator(unittest.TestCase):
    def test_calculate_tip(self):
        self.assertAlmostEqual(calculate_tip(100, 15), 15.0)

    def test_calculate_tip_zero_percent(self):
        self.assertAlmostEqual(calculate_tip(80, 0), 0.0)

    def test_grand_total(self):
        self.assertAlmostEqual(grand_total(100, 15), 115.0)

    def test_per_person_splits_evenly(self):
        self.assertAlmostEqual(per_person(120, 4), 30.0)

    def test_per_person_rejects_zero_people(self):
        with self.assertRaises(ValueError):
            per_person(100, 0)


if __name__ == "__main__":
    unittest.main()
