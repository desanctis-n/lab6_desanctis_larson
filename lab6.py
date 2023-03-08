# Nicholas DeSanctis

def encode(password):
    encoded = ''
    for i in password:
        if int(i) <= 6:
            encoded += str(int(i) + 3)
        else:
            encoded += str((int(i) + 3) % 10)
    return encoded


if __name__ == '__main__':
    loop_stop = False
    while not loop_stop:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')

        user_opt = int(input("Please enter an option: "))
        if user_opt == 1:
            encoded_password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

        elif user_opt == 2:
            pass

        elif user_opt == 3:
            loop_stop = True
