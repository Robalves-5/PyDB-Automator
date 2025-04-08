# 🚀 PyDB-Automator

**PyDB-Automator** é um projeto desenvolvido em Python com o objetivo de facilitar tarefas rotineiras de manipulação de dados em bancos SQL Server.  
Ele permite executar, de forma automatizada, as principais operações de um CRUD (Create, Read, Delete) com segurança, rapidez e sem a necessidade de abrir o SSMS (SQL Server Management Studio).

Ideal para analistas, desenvolvedores e profissionais que lidam com dados e desejam uma solução leve e eficiente para interagir com o banco via terminal ou scripts Python.

---

## 🛠️ O que esse projeto faz?

- 📥 **Inserção automática** de dados em tabelas específicas do banco (`INSERT`)
- 🔍 **Consultas SQL com agrupamentos e filtros** com saída formatada diretamente no terminal (`SELECT`)
- 🗑️ **Exclusão de registros com base em critérios definidos** (`DELETE`)
- 🤝 Integração com o SQL Server via `pyodbc`
- 💻 Fácil de configurar, executar e adaptar para novos cenários

---

## 🚀 Quando usar?

- Testes de performance e inserção rápida de registros
- Automatização de tarefas repetitivas em bancos de dados
- Análises rápidas de agrupamento e contagem
- Projetos de integração entre Python e SQL

---

## 📚 Requisitos

- Python 3.x
- SQL Server (local ou remoto)
- Bibliotecas:
  - `pyodbc`
  - `prettytable` (para exibição formatada dos dados)

Instale com:

```bash
pip install -r requeriments.txt


📦 PyDB-Automator/
├── 📄 README.md
├── 📄 .gitignore
├── 📄 requeriments.txt
├── 📄 Automaçao insert.py
├── 📄 Automaçao delete.py
├── 📄 Consulta.py
