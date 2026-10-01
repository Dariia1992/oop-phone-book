# 📒 OOP Phone Book

A console-based Phone Book application built with Python using Object-Oriented Programming (OOP).

The application allows users to manage contacts and stores all data in a CSV file.

## 🚀 Features

- Show all contacts
- Find contacts by:
  - Name
  - ID
  - Phone number
- Add new contacts
- Update existing contacts
- Delete contacts
- Automatic contact ID generation
- Input validation
- CSV data storage
- Automatic saving after changes

## 🛠 Technologies

- Python
- Object-Oriented Programming (OOP)
- CSV
- Git
- GitHub

## 📁 Project Structure

```text
oop-phone-book/
├── models/
│   ├── __init__.py
│   └── contact.py
│
├── services/
│   ├── __init__.py
│   └── phone_book.py
│
├── contact.csv
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Dariia1992/oop-phone-book.git
```

### 2. Open the project directory

```bash
cd oop-phone-book
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Run the application

```bash
python main.py
```

## 📋 Main Menu

```text
===== PHONE BOOK =====
1. Show all contacts
2. Find contact
3. Add contact
4. Update contact
5. Delete contact
0. Exit
======================
```

## 🔎 Contact Search

Contacts can be searched by:

- Name
- ID
- Phone number

## 💾 Data Storage

Contacts are stored in `contact.csv`.

The application loads contacts from the CSV file when it starts and saves changes after adding, updating, or deleting a contact.

## 🧠 What I Practiced

- Python classes and objects
- `__init__` and `self`
- Class methods
- Lists of objects
- Reading and writing CSV files
- `csv.DictReader`
- `csv.DictWriter`
- Loops and conditions
- Functions and `return`
- Input validation
- CRUD operations
- Working with multiple Python modules
- Virtual environments
- Git and GitHub

## 📚 CRUD Operations

- **Create** - add a new contact
- **Read** - show and search contacts
- **Update** - edit an existing contact
- **Delete** - remove a contact

## 👩‍💻 Author

Daria  
GitHub: Dariia1992