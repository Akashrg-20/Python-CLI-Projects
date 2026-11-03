# Python Contact Book CLI

A command-line Contact Book application built using Python and SQLite.

## Features

- Add new contacts
- View all contacts
- Search contacts by name or phone number
- Update contact details
- Delete individual contacts
- Delete all contacts with confirmation
- Phone number validation
- SQLite database storage

## Technologies Used

- Python
- SQLite3
- SQL

## Project Structure

```text
ContactBook/
├── main.py
├── contact.py
├── database.py
├── contacts.db
└── README.md
```

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run:

```bash
python main.py
```

The application automatically creates the SQLite database and CONTACTS table when configured in `database.py`.

## Learning Outcomes

- Python functions and classes
- Object-oriented programming basics
- SQLite database operations
- CRUD operations
- Exception handling
- Input validation

## Future Improvements

- Export contacts to CSV
- Display contacts in formatted tables
- Sort contacts alphabetically
- Add contact confirmation before deletion
