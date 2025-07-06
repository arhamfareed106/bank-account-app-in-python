# 🏦 CLI Bank System

This is a simple command-line based Bank System implemented in Python. It allows users to create and manage basic banking functions such as creating accounts, depositing and withdrawing money, and tracking transactions. All data is stored in a local `data.json` file.

## 📁 Features

* Create a new bank account with name, age, email, and a 4-digit PIN
* Deposit money (max ₹10,000 per transaction)
* Withdraw money with balance check
* View account details (secured with PIN)
* View last transaction history
* Update account name, email, and PIN
* Delete account
* Persistent data storage using `JSON`

## 💻 Technologies Used

* Python 3.x
* Built-in modules: `json`, `random`, `string`, `datetime`, `pathlib`

## 🚀 How to Run

1. **Clone or Download** this repository
2. Make sure Python is installed:

   ```bash
   python --version
   ```
3. **Run the script**:

   ```bash
   python bank_cli_app.py
   ```

## 🧪 Sample Run

```
Welcome to the Bank System
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Show Details
5. Show Transaction History
6. Update Details
7. Delete Account
8. Exit
```

## 📌 Data Storage

All user and transaction data is stored in a file named `data.json` in the same directory.

## 🔐 Security Note

* This is a demo application and does not include advanced security features like password hashing or encryption.
* Not suitable for production use without security enhancements.

## 📄 License

This project is open-source and free to use.

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

Created by [Arham Fareed](https://github.com/ArhamFareed)
