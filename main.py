import pyperclip
import os

FILE_NAME = "Password.txt"

def save_password():
    website = input("Enter the website: ")
    password = input("Enter the password: ")

    with open(FILE_NAME, 'a') as file:
        file.write(f"{website}<||>{password}\n")
    print("Password saved successfully.")
    


def get_password():
    website = input("Enter the website: ")
    with open(FILE_NAME, 'r') as file:
        for line in file:
            if website in line:
                password = line.split("<||>")[1].strip()
                pyperclip.copy(password)
                print("Password copied to clipboard.")
                break
        else:
            print("Website not found.")



def main():
    while True:
        print("1. Save a password")
        print("2. Get a password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            save_password()
        elif choice == '2':
            get_password()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()