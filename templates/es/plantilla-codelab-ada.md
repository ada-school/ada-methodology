# 🧪 Plantilla de Codelab ADA

Esta plantilla de codelab está diseñada siguiendo la Metodología ADA y la estructura de Átomos de Aprendizaje. Cada codelab debe combinar explicación, demostración de código y ejercicios guiados.

> **Dónde encaja:** un codelab es un átomo de 🧪 **Práctica** que construye una 🛠️ **Habilidad**
> (el *saber-hacer* que alguien debe realizar). Úsalo dentro de un Micro Curso creado con la
> [Plantilla de Micro-Credencial](plantilla-microcredencial-ada.md) — registra qué átomo/objetivo
> apoya y evalúalo con la **rúbrica de habilidad / desempeño**.

| Encaja en | Valor |
| --------- | ----- |
| Micro-credencial | \[título del curso] |
| Apoya átomo / objetivo | \[Átomo #, objetivo] |
| Tipo KSA / nivel objetivo | 🛠️ Habilidad · \[0–4] |

---

## 🧠 Título
Ejemplo: Crea tu primera API REST con Flask

## 🎯 Objetivo de Aprendizaje
Al finalizar este codelab, el estudiante será capaz de:
- Crear una API REST básica usando Flask
- Manejar métodos y rutas HTTP
- Ejecutar y probar una API localmente

---

## 🛠️ Requisitos
- Python 3.8+
- `pip`
- IDE o editor de código (por ejemplo, VS Code)

Instalar Flask:
```bash
pip install flask
```

---

## 🚀 Paso 1: API Hola Mundo
### 🔍 Explicación
Comenzaremos creando una aplicación mínima con Flask.

### 💻 Código de ejemplo
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, mundo!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 🧪 Ejercicio
- Ejecuta la app localmente
- Visita `http://127.0.0.1:5000/`
- Cambia el texto de respuesta por tu nombre

---

## 📨 Paso 2: Agregar una nueva ruta
### 🔍 Explicación
Ahora crearemos una ruta que devuelva información de usuario.

### 💻 Código de ejemplo
```python
@app.route('/usuario')
def usuario():
    return {'nombre': 'Jane Doe', 'edad': 28}
```

### 🧪 Ejercicio
- Agrega otra ruta `/acerca` que devuelva un mensaje breve sobre ti.

---

## 🧪 Desafío Final
Crea una ruta `/saludo/<nombre>` que devuelva `¡Hola, <nombre>!`.

Ejemplo:
```python
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"¡Hola, {nombre}!"
```

Pruébalo en: `http://127.0.0.1:5000/saludo/Ada`

---

## ✅ Criterios de Finalización
- [ ] La aplicación corre sin errores
- [ ] Todas las rutas funcionan correctamente
- [ ] La ruta personalizada responde dinámicamente

---

## 🏁 Próximos Pasos
- Usa `jsonify` para devolver respuestas JSON
- Publica tu app con Replit o Render
- Explora Flask Blueprints para APIs modulares

---

> Puedes duplicar esta plantilla para crear tus propios codelabs alineados con la metodología ADA en cualquier tecnología.