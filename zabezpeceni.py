"""
autor = Alex Olivier Michaud
This is a simple login system using python and sqlite3
"""
import hashlib
from getpass import getpass
from sqlite3 import connect

db = connect('users_passw.db')
db.execute('CREATE TABLE IF NOT EXISTS passwd (name TEXT, password TEXT)')

def hash_password(name, password):
    hash = hashlib.sha256(password.encode('utf-8'))
    query = 'SELECT * FROM passwd WHERE password = ?', (hash.hexdigest())
    if query:
        return True
    else:
        return False

def new_user(name, password):
    hash = hashlib.sha256(password.encode('utf-8'))
    query = 'INSERT INTO passwd VALUES (?, ?)', (name, hash.hexdigest())
    db.execute(*query)
    db.commit()
    return True

if __name__ == '__main__':
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter your name: ")
            password = getpass("Enter your password: ")
            if hash_password(name, password):
                print("Login successful")
        elif choice == '2':
            name = input("Enter your name: ")
            password = getpass("Enter your password: ")
            new_user(name, password)
        elif choice == '3':
            break










