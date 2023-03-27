def printMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encodePass(data):
    res = ""
    for i in data:
        temp = int(i) + 3
        if temp > 9:
            temp = temp % 10
        res = res + str(temp)
    return res

def decodePass(encryptedCode):
    res = ""
    for i in encryptedCode:
        temp = int(i) - 3
        if temp < 1:
            temp = abs(temp % 10)
        res = res + str(temp)
    return res

if __name__ == "__main__":
    while True:
        printMenu()
        option = int(input("Please enter an option: "))
        if option == 1:
            data = (input("Please enter your password to encode: "))
            encryptedCode = encodePass(data)
            print("Your password has been encoded and stored!")
        if option == 2:
            print(f"The encoded password is {encryptedCode}, and the original password is {decodePass(encryptedCode)}.")
        if option == 3:
            break
