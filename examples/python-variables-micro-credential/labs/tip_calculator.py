"""Atom 4 lab — expressions, conversion & f-strings, made testable.

Pure functions for the math, ``main()`` for input/output.

Run it:     python3 tip_calculator.py
Run tests:  python3 -m unittest test_tip_calculator.py
"""


def calculate_tip(bill, tip_percent):
    """Return the tip amount for a bill and a tip percentage."""
    return bill * tip_percent / 100


def grand_total(bill, tip_percent):
    """Return the bill plus tip."""
    return bill + calculate_tip(bill, tip_percent)


def per_person(total, people):
    """Return each person's share. Raises ValueError if people <= 0."""
    if people <= 0:
        raise ValueError("people must be greater than 0")
    return total / people


def main():
    bill = float(input("Bill amount? "))
    tip_percent = int(input("Tip %? "))
    people = int(input("Split between how many? "))

    tip = calculate_tip(bill, tip_percent)
    total = grand_total(bill, tip_percent)
    each = per_person(total, people)

    print(f"Bill:        ${bill:.2f}")
    print(f"Tip ({tip_percent}%):    ${tip:.2f}")
    print(f"Grand total: ${total:.2f}")
    print(f"Each person pays: ${each:.2f}")


if __name__ == "__main__":
    main()
