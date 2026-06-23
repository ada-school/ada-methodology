"""Unit tests for profile_card.py (Atom 3).

Run:  python3 -m unittest test_profile_card.py
"""
import unittest

from profile_card import calculate_age, make_profile_card


class TestProfileCard(unittest.TestCase):
    def test_calculate_age(self):
        self.assertEqual(calculate_age(1990, 2026), 36)

    def test_calculate_age_same_year_is_zero(self):
        self.assertEqual(calculate_age(2026, 2026), 0)

    def test_card_contains_all_fields(self):
        card = make_profile_card("Ada", 2000, "Python", 2026)
        self.assertIn("Ada", card)
        self.assertIn("26", card)          # age 2026 - 2000
        self.assertIn("Python", card)

    def test_card_is_multiline(self):
        card = make_profile_card("Grace", 1906, "COBOL", 2026)
        self.assertEqual(len(card.splitlines()), 4)


if __name__ == "__main__":
    unittest.main()
