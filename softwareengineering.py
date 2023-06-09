def main():
    en = ""
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        user = int(input("Please enter an option: "))
        if user == 3:
            break
        elif user == 1:
            og = (input("Please enter your password to encode: "))
            en = encoder(og)
            print("Your password has been encoded and stored!")
        elif user == 2:
            print(f"The encoded password is {en}, and the original password is {decoder(en)}.")

def decoder(encoded): # Pedro Leon ;)
    password = ""
    for digit in encoded:
        # Shift the digit down by 3 numbers
        shifted_digit = str((int(digit) - 3) % 10)
        password += shifted_digit
    return password

def encoder(password): #Fernando Hernandez Martin
    encoded = ""
    for digit in password:
        if int(digit) <= 6:
            encoded += str(int(digit) + 3)
        else:
            encoded += str((int(digit) + 3) % 10)
    return encoded

if __name__ == '__main__':
    main()


