# 🧪 Modelo de Codelab ADA

Este modelo de codelab é projetado seguindo a Metodologia ADA e a estrutura de Átomos de Aprendizado. Cada codelab deve combinar explicação, demonstração de código e exercícios guiados.

---

## 🧠 Título
Exemplo: Construa Sua Primeira API REST com Flask

## 🎯 Objetivo de Aprendizado
Ao final deste codelab, os aprendizes serão capazes de:
- Criar uma API REST básica usando Flask
- Lidar com métodos HTTP e rotas
- Executar e testar uma API localmente

---

## 🛠️ Requisitos
- Python 3.8+
- `pip`
- IDE ou editor de código (ex., VS Code)

Instalar Flask:
```bash
pip install flask
```

---

## 🚀 Passo 1: API Hello World
### 🔍 Explicação
Começaremos construindo uma aplicação Flask mínima.

### 💻 Exemplo de Código
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, mundo!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 🧪 Exercício
- Execute a aplicação localmente
- Visite `http://127.0.0.1:5000/`
- Mude o texto de resposta para o seu nome

---

## 📨 Passo 2: Adicione uma Nova Rota
### 🔍 Explicação
Vamos criar uma nova rota que retorna informações do usuário.

### 💻 Exemplo de Código
```python
@app.route('/usuario')
def usuario():
    return {'nome': 'João Silva', 'idade': 28}
```

### 🧪 Exercício
- Adicione outra rota `/sobre` que retorna uma mensagem curta sobre você.

---

## 🧪 Desafio Final
Crie um endpoint `/saudar/<nome>` que retorna `Olá, <nome>!`.

Exemplo:
```python
@app.route('/saudar/<nome>')
def saudar(nome):
    return f"Olá, {nome}!"
```

Teste com: `http://127.0.0.1:5000/saudar/Ada`

---

## ✅ Critérios de Conclusão
- [ ] A aplicação executa sem erros
- [ ] Todos os endpoints funcionam conforme esperado
- [ ] A rota personalizada retorna conteúdo dinâmico

---

## 🏁 Próximos Passos
- Adicionar respostas JSON usando `jsonify`
- Fazer deploy da aplicação com Replit ou Render
- Explorar Flask Blueprints para APIs modulares

---

> Você pode duplicar este modelo para construir seus próprios codelabs alinhados com ADA em qualquer domínio.