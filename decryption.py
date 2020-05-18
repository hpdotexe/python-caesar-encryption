def decrypt(text, s):
    result = ''

    # transverse the Cipher

    for i in range(len(text)):
        char = text[i]

                        # Decrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():

                        # Decrypt lowercase characters in plain text

            result += chr((ord(char) - s - 97) % 26 + 97)
        elif ord(char) <= 64 and ord(char) >= 32:

                        # Decrypt common special characters

            result += chr((ord(char) - s - 32) % 33 + 32)
        else:

                        # Rest all symbols remain the same

            result += char
    return result


text = input('Enter the Cipher : ')
s = int(input('Enter shift pattern : '))

print ('Cipher : ' + text)
print ('Shift pattern : ' + str(s))
print ('Plain text : ' + decrypt(text, s))	
