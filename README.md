# Password Manager (CLI)

A lightweight command-line password manager written in Python. The application stores account names and encrypted passwords in local text files and supports create, read, update, and delete operations.

## Overview

This project uses the `cryptography` library (`Fernet`) to encrypt passwords before storing them. Records are managed through an interactive terminal menu.

## Features

- Add one or more account/password entries
- Encrypt passwords before storage
- View (decrypt) a password for a selected account
- Update password for an existing account
- Delete an account record

## Project Structure

- `main.py`: Application entry point and CLI logic
- `Account_Info.txt`: Stores account names (one per line)
- `Key_Password_Info.txt`: Stores encryption key and encrypted password pairs

## Requirements

- Python 3.8+
- `cryptography` package

## Installation

1. Clone or download this repository.
2. Install dependencies:

```bash
pip install cryptography
```

## Usage

Run the program from the project root:

```bash
python main.py
```

Menu options:

- `1` Entry: Add new account/password records
- `2` Extract: Display saved accounts and decrypt selected password
- `3` Update: Replace the password for a selected account
- `4` Delete: Remove a selected account/password record
- `0` Exit: Close the application

## Data Format

- `Account_Info.txt`
  - One account name per line
- `Key_Password_Info.txt`
  - One line per record in the format:
  - `<fernet_key>,<encrypted_password>`

## Security Notes

This implementation is educational and not production-grade:

- Encryption keys are stored alongside encrypted passwords.
- Files are stored in plain local text files without OS-level secret storage.
- There is no master password, access control, or audit logging.

For real-world usage, move key management to a secure vault/KMS and protect records with stronger authentication controls.

## Known Limitations

- Input validation is minimal (invalid menu/index input can raise runtime errors).
- Record consistency relies on line alignment between the two data files.
