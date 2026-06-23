## ⚛ Learning Atom 4 — *Expressions, Conversion & f-strings (Codelab)*

**Phase:** 🙊 3 · Applied Practice (*do*) · **KSA:** 🛠️ Skill (+ 🌱 Ability) · **Target level:** L2
· **Component ids:** `S-use-values`, `A-attention-detail`

### 🎯 Learning objective

- **Use** variables in expressions, **convert** types safely, and **format** output with
  f-strings to build a small interactive script.

### 🧩 Prerequisites

- Atoms 1–3. A Python runner open.

### 🧭 Atom description

Storing data is only useful if you *do* something with it. This codelab is where variables pay
off: you combine them in expressions, take user input, convert it to the right type, and print
clean, readable results with **f-strings** — the modern, professional way to format output.

---

### 🎬 Watch — f-strings in Python (short)

```youtube
https://www.youtube.com/watch?v=Mfmr_Puhtwc
"Python f-strings" — formatting values into text the modern way (~7 min).
```

### 📖 Read — *Expressions, conversion & f-strings* (≈ 5 min)

**Arithmetic operators** you'll use with number variables:

| Op | Means | Example | Result |
| -- | ----- | ------- | ------ |
| `+ - *` | add, subtract, multiply | `3 * 4` | `12` |
| `/` | divide (always a float) | `7 / 2` | `3.5` |
| `//` | floor divide | `7 // 2` | `3` |
| `%` | remainder (modulo) | `7 % 2` | `1` |
| `**` | power | `2 ** 3` | `8` |

You can update a variable using itself with **augmented assignment**:

```python
total = 100
total += 20      # same as total = total + 20  → 120
total *= 2       # → 240
```

**f-strings** put variables straight into text. Prefix the string with `f` and wrap names in `{}`:

```python
name = "Ada"
score = 92.5
print(f"{name} scored {score} points.")          # Ada scored 92.5 points.
print(f"{name} scored {score:.1f} points.")      # 92.5  (.1f = 1 decimal place)
print(f"Next year bonus: {score * 1.1:.2f}")     # expressions work inside {}
```

Remember the **input → convert → use** pattern from Atom 2:

```python
price = float(input("Price? "))      # "19.99" → 19.99
qty   = int(input("Quantity? "))     # "3" → 3
total = price * qty
print(f"Total for {qty} items: ${total:.2f}")
```

---

### 💻 Codelab — build a tip calculator

Build it step by step; run after each step.

```python
# Step 1 — gather inputs (convert as you read)
bill = float(input("Bill amount? "))
tip_percent = int(input("Tip %? "))
people = int(input("Split between how many? "))

# Step 2 — compute with expressions
tip = bill * tip_percent / 100
grand_total = bill + tip
per_person = grand_total / people

# Step 3 — format the output with f-strings
print(f"Bill:        ${bill:.2f}")
print(f"Tip ({tip_percent}%):    ${tip:.2f}")
print(f"Grand total: ${grand_total:.2f}")
print(f"Each person pays: ${per_person:.2f}")
```

**Extend it (choose at least one):**

- Add a `tax_percent` and include tax before the tip.
- Use `//` and `%` to show the result as whole dollars and remaining cents.
- Print a one-line summary using a single f-string.

---

### 🧪 AI Prompt Question (practice with AI, then verify)

Ask an AI assistant:

```prompt
"Explain step by step why this Python code raises a TypeError, and give the corrected version:

    age = input('Age? ')
    print('Next year you will be ' + age + 1)

Then explain the rule about input() and type conversion in one sentence."
```

> 🤖 **Human-in-the-loop:** don't just paste the answer — *run* the corrected code and confirm it.
> The bug is that `input()` returns a string and you can't `+ 1` to a string (and can't `+` a
> string and int). Fix: `age = int(input('Age? '))` then use an f-string.

---

### 💻🧪 Lab with tests — *refactor into functions, add a `main()`, verify*

The version above mixes math and input. Refactor the math into **pure functions** (no `input`,
no `print` — just take values, return values), keep the I/O in `main()`, and write **unit tests**
so you can prove the calculator is correct.

> 📁 Runnable files: [`../labs/tip_calculator.py`](../labs/tip_calculator.py) and
> [`../labs/test_tip_calculator.py`](../labs/test_tip_calculator.py).

```python
# tip_calculator.py
def calculate_tip(bill, tip_percent):
    return bill * tip_percent / 100

def grand_total(bill, tip_percent):
    return bill + calculate_tip(bill, tip_percent)

def per_person(total, people):
    if people <= 0:
        raise ValueError("people must be greater than 0")
    return total / people

def main():
    bill = float(input("Bill amount? "))
    tip_percent = int(input("Tip %? "))
    people = int(input("Split between how many? "))
    total = grand_total(bill, tip_percent)
    print(f"Grand total: ${total:.2f}")
    print(f"Each person pays: ${per_person(total, people):.2f}")

if __name__ == "__main__":
    main()
```

```python
# test_tip_calculator.py
import unittest
from tip_calculator import calculate_tip, grand_total, per_person

class TestTipCalculator(unittest.TestCase):
    def test_calculate_tip(self):
        self.assertAlmostEqual(calculate_tip(100, 15), 15.0)

    def test_grand_total(self):
        self.assertAlmostEqual(grand_total(100, 15), 115.0)

    def test_per_person_splits_evenly(self):
        self.assertAlmostEqual(per_person(120, 4), 30.0)

    def test_per_person_rejects_zero_people(self):
        with self.assertRaises(ValueError):    # bad input should error, not divide by zero
            per_person(100, 0)

if __name__ == "__main__":
    unittest.main()
```

```bash
python3 tip_calculator.py                      # run it
python3 -m unittest test_tip_calculator.py     # run the tests → "OK"
```

> 💡 Use `assertAlmostEqual` for `float` math (decimals can carry tiny rounding error, so `==` is
> unreliable). Notice the test for *bad input* — robust code expects mistakes.

---

### ✅ Evaluate — Performance task (`skill`)

Predict the output **before** running, then verify:

```python
a = 7
b = 2
print(a / b, a // b, a % b, a ** b)

label = "ada"
print(f"{label.upper()} x3 = {label * 3}")

x = "10"
print(int(x) + 5)
```

<details>
<summary>Answer key</summary>

- `3.5 3 1 49` — true divide, floor divide, remainder, power.
- `ADA x3 = adaadaada`.
- `15` — `x` is the string `"10"`, converted with `int()` then `+ 5`.

</details>

---

### 📦 Deliverable

- Your working **tip calculator** (with at least one extension), pasted with a sample run. Output
  must use f-strings and show money to 2 decimals.

### 🧬 Skill check (what "L2" looks like)

- [ ] Reads input and **converts** it to the right type before computing.
- [ ] Uses at least three different operators correctly.
- [ ] Output is formatted with f-strings (`:.2f` for money).
- [ ] You diagnosed the AI Prompt Question bug as an `input()`/type issue.

### 🧠 Final reflection

- Where did a type conversion (or a missing one) bite you? How will you spot it faster next time?

### 🔗 Sources to verify (human-in-the-loop)

- Python docs — *Formatted string literals (f-strings)* and *Format Specification Mini-Language*.
- Python tutorial §3 — *Numbers* (operators, `/` vs `//` vs `%`).

### 🧩 Connections

- **Predecessors:** Atoms 1–3. **Successors:** Atom 5 (ship a small program of your own).
