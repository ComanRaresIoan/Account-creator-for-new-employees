import random
import string

def create_password(length=12):
    Digits = '1234567890'
    lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    specialchar = '!@#$%^&*()_+{}|":<>?/*-'

    password = ''.join([
        random.choice(Digits),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(specialchar),
        random.choice(Digits),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(specialchar),
        random.choice(Digits),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(specialchar)
    ])
    return password

def create_user():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    gender = input("Enter the gender (1 for Male, 2 for Female): ")
    if gender == '1':
        gender = 'Male'
    elif gender == '2':
        gender = 'Female'
    else:
        print("Error, Gender not provided")
    age = int(input("Enter your age: "))
    company_name = input("Enter the company's name: ")

    email = f"{first_name.lower()}{last_name.lower()}@{company_name.lower()}.com"
    filename = f"{first_name.lower()}{last_name.lower()}_information.txt"

    data = [first_name, last_name, gender, str(age), company_name]

    with open(filename, 'w') as file:
        for item, value in zip(["First Name", "Last Name", "Gender", "Age", "Company Name"], data):
            file.write(f"Your {item} is: {value}\n")

        file.write("Your email is: " + email + "\n")
        file.write("Your password is: " + create_password() + "\n")

    print(f"The folder with the information has the name {filename} and can be found in this directory.")

create_user()