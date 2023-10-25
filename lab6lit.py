#encode function for menu
def encode(string):
    def encode(string):
        numbers = []
        encodednum = ''
        for i in range(len(string)):
            numbers.append(int(string[i]) + 3)
        for j in range(len(numbers)):
            encodednum += str(numbers[j])
            return encodednum

def decode():
    print("The encoded password is ", encodednum, ", and the original password is ", password)

#main function for menu
if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("\nPlease enter an option: "))

        if option == 1:
            password = str(input("Please enter your password to encode: "))
            encode(password)
            print("Your password has been encoded and stored!\n")

            continue

        if option == 2:
            continue

