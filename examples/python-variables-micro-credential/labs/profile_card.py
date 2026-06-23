"""Atom 3 lab — naming & assignment, made testable.

The logic lives in small, well-named functions (easy to unit-test); ``main()`` handles the
input/output so the functions stay pure.

Run it:     python3 profile_card.py
Run tests:  python3 -m unittest test_profile_card.py
"""


def calculate_age(birth_year, current_year):
    """Return age in whole years for a given birth year and current year."""
    return current_year - birth_year


def make_profile_card(name, birth_year, favorite_language, current_year):
    """Return a formatted, multi-line profile card string."""
    age = calculate_age(birth_year, current_year)
    return (
        "----- PROFILE -----\n"
        f"Name:     {name}\n"
        f"Age:      {age}\n"
        f"Codes in: {favorite_language}"
    )


def main():
    name = input("Name? ")
    birth_year = int(input("Birth year? "))
    favorite_language = input("Favorite language? ")
    current_year = 2026
    print(make_profile_card(name, birth_year, favorite_language, current_year))


if __name__ == "__main__":
    main()
