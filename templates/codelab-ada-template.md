# 🧪 ADA Codelab Template

This codelab template is designed following the ADA Methodology and Learning Atoms structure. Each codelab should combine explanation, code demonstration, and guided exercises.

---

## 🧠 Title
Example: Build Your First REST API with Flask

## 🎯 Learning Objective
By the end of this codelab, learners will be able to:
- Create a basic REST API using Flask
- Handle HTTP methods and routes
- Run and test an API locally

---

## 🛠️ Requirements
- Python 3.8+
- `pip`
- IDE or code editor (e.g., VS Code)

Install Flask:
```bash
pip install flask
```

---

## 🚀 Step 1: Hello World API
### 🔍 Explanation
We’ll start by building a minimal Flask application.

### 💻 Code Example
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 🧪 Exercise
- Run the app locally
- Visit `http://127.0.0.1:5000/`
- Change the response text to your name

---

## 📨 Step 2: Add a New Route
### 🔍 Explanation
Let’s create a new route that returns user info.

### 💻 Code Example
```python
@app.route('/user')
def user():
    return {'name': 'Jane Doe', 'age': 28}
```

### 🧪 Exercise
- Add another route `/about` that returns a short message about you.

---

## 🧪 Final Challenge
Create an endpoint `/greet/<name>` that returns `Hello, <name>!`.

Example:
```python
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"
```

Test it with: `http://127.0.0.1:5000/greet/Ada`

---

## ✅ Completion Criteria
- [ ] App runs without errors
- [ ] All endpoints work as expected
- [ ] Personalized route returns dynamic content

---

## 🏁 Next Steps
- Add JSON responses using `jsonify`
- Deploy the app with Replit or Render
- Explore Flask Blueprints for modular APIs

---

> You can duplicate this template to build your own ADA-aligned codelabs in any technology domain.

