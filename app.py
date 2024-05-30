import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_generator(length):
    if length <= 0:
        return "Please enter a valid number for the password length."
    else:
        return generate_password(length)
    
if __name__ == "__main__":
    n=int(input("Enter the Length of password: "))
    passw=password_generator(n)
    print(passw)
