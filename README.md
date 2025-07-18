# 💳 BankEasy

Welcome to **BankEasy**!  
A simple Python project to manage clients and accounts using PostgreSQL.

---

## 📦 Project Structure

```
BankEasy/
│
├── account.py      # Account operations
├── client.py       # Client operations
├── connect_db.py   # Database connection
├── main.py         # Main script
├── .gitignore      # Git ignore rules
└── README.md       # Project info
```

---

## 🚀 Features

- Add new clients and accounts
- View all clients and accounts
- Easy-to-understand code for beginners

---

## 🛠️ Requirements

- Python 3.8+
- PostgreSQL
- psycopg2 (`pip install psycopg2`)

---

## ⚡ Quick Start

1. **Clone the repo**
   ```
   git clone https://github.com/KhalilAmamri/BankEasy.git
   cd BankEasy
   ```

2. **Set up your database**
   - Create a PostgreSQL database named `bank_app`
   - Create tables:
     ```sql
     CREATE TABLE clients (
         client_id SERIAL PRIMARY KEY,
         name VARCHAR(100),
         email VARCHAR(100)
     );

     CREATE TABLE accounts (
         account_id SERIAL PRIMARY KEY,
         name VARCHAR(100),
         balance NUMERIC,
         client_id INTEGER REFERENCES clients(client_id)
     );
     ```

3. **Configure your connection**
   - Edit `connect_db.py` with your database credentials.

4. **Run the app**
   ```
   python main.py
   ```

---

## 📚 Usage

- To add a client or account, edit `main.py` as shown in the examples.
- All database logic is in `client.py` and `account.py`.

---

## 🖼️ Icons

- 💳 Banking
- 📦 Structure
- 🚀 Features
- 🛠️ Requirements
- ⚡ Quick Start
- 📚 Usage

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

[MIT](LICENSE)

---

## 👤 Author

- Khalil Amamri

---

> Made with ❤️ for learning and sharing!