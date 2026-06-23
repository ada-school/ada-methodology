"""Capstone lab (Atom 5) — a small "receipt maker" program, made testable.

Pure functions build the receipt; ``main()`` does the input/output.

Run it:     python3 receipt.py
Run tests:  python3 -m unittest test_receipt.py
"""

TAX_RATE = 0.19  # constant in UPPER_CASE


def subtotal(unit_price, quantity):
    """Return unit_price * quantity."""
    return unit_price * quantity


def apply_tax(amount, rate=TAX_RATE):
    """Return amount with tax added."""
    return amount * (1 + rate)


def build_receipt(item_name, unit_price, quantity, rate=TAX_RATE):
    """Return a formatted, multi-line receipt string."""
    sub = subtotal(unit_price, quantity)
    tax = sub * rate
    total = sub + tax
    return (
        "----- RECEIPT -----\n"
        f"{item_name} x{quantity} @ ${unit_price:.2f}\n"
        f"Subtotal: ${sub:.2f}\n"
        f"Tax ({rate * 100:.0f}%): ${tax:.2f}\n"
        f"TOTAL:    ${total:.2f}"
    )


def main():
    item_name = input("Item name? ")
    unit_price = float(input("Unit price? "))
    quantity = int(input("Quantity? "))
    print(build_receipt(item_name, unit_price, quantity))


if __name__ == "__main__":
    main()
