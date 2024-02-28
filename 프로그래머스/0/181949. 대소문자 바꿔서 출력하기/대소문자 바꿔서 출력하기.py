str = input()

list_str= list(str)
for char in list_str:
    temp = ord(char)
    if temp > 96:
        print(chr(temp - 32), end='')
    else:
        print(chr(temp + 32), end='')
             