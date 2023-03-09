
# Nicholas DeSanctis

def encode(password):
    encoded = ''
    for i in password:
        if int(i) <= 6:
            encoded += str(int(i) + 3)
        else:
            encoded += str((int(i) + 3) % 10)
    return encoded

def decoder(data):
    password=''
    for i in data:
        if int (i)==0:
            password+='7'
        if int(i)== 1:
            password+='8'
        if int(i)==2:
            password+='9'
        elif int(i)==3:
            password+='0'
        elif int(i)==4:
            password+='1'
        elif int(i)==5:
            password+='2'
        elif int(i)==6:
            password+='3'
        elif int(i)==7:
            password+='4'
        elif int(i)==8:
            password+='5'
        elif int(i)==9:
            password+='6'
    return password



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
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}.")
            print(decoder(encoded_password))

        elif user_opt == 3:
            loop_stop = True

