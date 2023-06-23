def IsDigit(char):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if char in digits:
        return True
    else:
        return False

string = input("Введите символ: ")
for char in string:
    if IsDigit(char):
        print(f"{char} - это цифра")
    else:
        print(f"{char} - это не цифра")