## ⚛ Learning Atom 3 — *Naming & Assignment (Codelab)*

**Phase:** 🙊 3 · Applied Practice (*do*) · **KSA:** 🛠️ Skill (+ 🌱 Ability) · **Target level:** L2
· **Component ids:** `S-declare-assign`, `A-attention-detail`

### 🎯 Learning objective

- **Declare, assign, and reassign** variables using **valid, readable PEP 8 names**, and fix the
  common naming/assignment errors by reading the error message.

### 🧩 Prerequisites

- Atoms 1–2. A Python runner open ([replit.com](https://replit.com), Colab, or local `python3`).

### 🧭 Atom description

Now you write code. Good variable *names* are not cosmetic — they are how code stays
understandable (to your teammates and to future-you). This codelab drills the mechanics of
assignment and the naming rules until they're automatic, and trains the habit of reading errors
instead of guessing.

---

### 📖 Read — *Naming rules & conventions* (≈ 4 min)

**Hard rules (break these and Python errors):**

- A name may contain letters, digits, and underscores `_`, and **cannot start with a digit**.
- No spaces and no operators in a name (`my var`, `my-var` are invalid).
- Names are **case-sensitive**: `age`, `Age`, and `AGE` are three different variables.
- You can't use Python **keywords** as names (`if`, `for`, `class`, `True`, `def`, `list`…).

**Conventions (PEP 8 — the style that makes you look professional):**

- Use **`snake_case`**: lowercase words joined by underscores → `first_name`, `total_price`.
- Make names **descriptive**: `n` < `num` < `num_students`. Future-you will thank you.
- Constants you won't change go in **`UPPER_CASE`** → `TAX_RATE = 0.19`.
- Avoid shadowing built-ins: don't name a variable `list`, `str`, `sum`, `type`, or `input`.

```python
# 👎 hard to read / risky
x = 19.99
l = 3
str = "hi"          # shadows the built-in str() — now str(5) breaks!

# 👍 clear and safe
unit_price = 19.99
quantity = 3
greeting = "hi"
TAX_RATE = 0.19
```

**Multiple & swap assignment** (handy Python shortcuts):

```python
a, b = 1, 2          # assign several at once
a, b = b, a          # swap! a is now 2, b is now 1 — no temp variable needed
x = y = 0            # both x and y refer to 0
```

---

### 💻 Codelab — *step by step*

Type each step yourself (don't copy-paste) — the muscle memory is the point.

**Step 1 — declare & print**

```python
first_name = "Ada"
birth_year = 1815
print(first_name, "was born in", birth_year)
```

**Step 2 — reassign & compute an age**

```python
current_year = 2026
age = current_year - birth_year
print(first_name, "would be", age, "years old.")
birth_year = 1820          # reassign
age = current_year - birth_year
print("Corrected age:", age)
```

**Step 3 — multiple assignment & swap**

```python
left, right = "🍎", "🍊"
print("Before:", left, right)
left, right = right, left
print("After: ", left, right)
```

**Step 4 — fix the broken code (read the error!)**
Each line below has one bug. Run it, read the error, and fix it.

```python
2nd_place = "silver"        # SyntaxError — why? (rename it)
first name = "Grace"        # SyntaxError — why?
print(First_name)           # NameError — why? (look at the capital F)
TAX RATE = 0.19             # SyntaxError — fix the name
```

<details>
<summary>Fixes</summary>

```python
second_place = "silver"     # names can't start with a digit
first_name = "Grace"        # no spaces in names → use snake_case
print(first_name)           # case-sensitive: First_name ≠ first_name
TAX_RATE = 0.19             # no spaces; constants in UPPER_CASE
```
</details>

---

### 💻🧪 Lab with tests — *put the logic in a function and prove it works*

Real code is organized into **functions** and verified with **unit tests**. Move your age logic
into a well-named function, add a `main()` to run it, and let a test confirm it's correct.

> 📁 Runnable files: [`../labs/profile_card.py`](../labs/profile_card.py) and
> [`../labs/test_profile_card.py`](../labs/test_profile_card.py).

```python
# profile_card.py — logic in functions, I/O in main()
def calculate_age(birth_year, current_year):
    return current_year - birth_year

def make_profile_card(name, birth_year, favorite_language, current_year):
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
    print(make_profile_card(name, birth_year, favorite_language, 2026))

if __name__ == "__main__":   # only runs when you execute the file directly
    main()
```

The test file checks the functions *without* asking for input (that's why the logic is separate
from `main()`):

```python
# test_profile_card.py
import unittest
from profile_card import calculate_age, make_profile_card

class TestProfileCard(unittest.TestCase):
    def test_calculate_age(self):
        self.assertEqual(calculate_age(1990, 2026), 36)

    def test_card_contains_all_fields(self):
        card = make_profile_card("Ada", 2000, "Python", 2026)
        self.assertIn("Ada", card)
        self.assertIn("26", card)
        self.assertIn("Python", card)

if __name__ == "__main__":
    unittest.main()
```

Run them from the `labs/` folder:

```bash
python3 profile_card.py                     # run the program
python3 -m unittest test_profile_card.py    # run the tests  → "OK"
```

> 🧠 **Why test?** `assertEqual(calculate_age(1990, 2026), 36)` says *"I expect this answer."* If a
> later edit breaks it, the test fails immediately — that's the **attention-to-detail / debugging
> habit** (`A-attention-detail`) made automatic.

---

### ✅ Evaluate — Skill mini-rubric (`skill`)

Which of these are **valid** Python variable names? For invalid ones, say why and rename.

`total_2`, `2total`, `total-price`, `totalPrice`, `class`, `_hidden`, `Total Price`

<details>
<summary>Answer key</summary>

- `total_2` ✅ valid.
- `2total` ❌ can't start with a digit → `total_2` or `second_total`.
- `total-price` ❌ `-` is an operator → `total_price`.
- `totalPrice` ✅ valid, but ⚠️ not PEP 8 → prefer `total_price`.
- `class` ❌ reserved keyword → `class_name` / `course_class`.
- `_hidden` ✅ valid (leading underscore is allowed).
- `Total Price` ❌ spaces not allowed → `total_price`.

</details>

---

### 📦 Deliverable

- A short script that: declares 4 well-named variables (mix of types), reassigns at least one,
  performs one swap, and prints clear output. Names must follow PEP 8 `snake_case`.

### 🧬 Skill check (what "L2" looks like)

- [ ] Every name is valid **and** descriptive `snake_case`.
- [ ] Reassignment and a swap both work and are explained in a comment.
- [ ] You fixed the Step 4 bugs by **reading the error type** (Syntax/Name), not by guessing.

### 🧠 Final reflection

- Rename one variable in your code to something better. What did the new name make obvious that
  the old one hid?

### 🔗 Sources to verify (human-in-the-loop)

- **PEP 8** — *Style Guide for Python Code* (naming conventions).
- Python docs — *Lexical analysis / Keywords* (the reserved words list).

### 🧩 Connections

- **Predecessors:** Atoms 1–2. **Successors:** Atom 4 (now *use* these variables).
