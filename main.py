#encode function made by Fabio Jorge Hernandez
def encode(password):
    encodedpsw = ""
    for digit in str(password):
        if str(int(digit) + 3) == "10":
            encodedpsw += "0"
        elif str(int(digit) + 3) == "11":
            encodedpsw += "1"
        elif str(int(digit) + 3) == "12":
            encodedpsw += "2"
        else:
            encodedpsw += str(int(digit) + 3)
    return encodedpsw

#main function made by Fabio Jorge Hernandez
def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encodedpassword = encode(password)
            print("Your password has been encoded and stored!\n")
            continue
        elif option == 2:
            print("The encoded password is " + encodedpassword + ", and the original password is " + password + ".\n")
            continue
        elif option == 3:
            break
        else:
            print("Choose a number in the menu.")

if __name__ == "__main__":
    main()
