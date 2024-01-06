def encrypt_decrypt(plain_text, k1, k2, k3, k4, k5):
    cipher_text = ""

    for i in range(0, len(plain_text), 4):
        chunk = plain_text[i:i+4].ljust(4, 'X')  # Padding with 'X' if the chunk is less than 4 characters

        k1_val, k2_val, k3_val, k4_val, k5_val = map(int, [k1, k2, k3, k4, k5]) # converting string to int

        for i in range(0,len(chunk)):
            char_val = ord(chunk[i]) - ord('a')  # Mapping 'a' to 0, 'b' to 1, and so on

            #performing operation to encrypt each character of chunk
            if(i==0):
              result = ((k3_val * k1_val) - char_val)
              if(result<0):
                result = result - (2*result)
              result = result % 26

            elif(i==1):
              result = ((k3_val * k2_val) - char_val)
              if(result<0):
                result = result - (2*result)
              result = result % 26

            elif(i==2):
              result = ((k3_val * k5_val) - char_val)
              if(result<0):
                result = result - (2*result)
              result = result % 26

            elif(i==3):
              result = ((k3_val * k4_val) - char_val)
              if(result<0):
                result = result - (2*result)
              result = result % 26


            cipher_text += chr(result + ord('a'))  # Mapping back to characters

    return cipher_text #after looping through all chunks it will return final cipher string


#---------main------------

# Encrypt or decrypt the plaintext/ciphertext
choice = int(input("\nWhat do you want to do\n1) Encryption(press 1)\n2) Decryption(press 2)\n"))
# Get keys and plaintext from the user
k1 = input("Enter key k1: ")
k2 = input("Enter key k2: ")
k3 = input("Enter key k3: ")
k4 = input("Enter key k4: ")
k5 = input("Enter key k5: ")
if(choice==1):
    plaintext = input("Enter the plaintext: ").replace(" ", "").lower()  # Removing spaces and converting to lowercase
    cipher_result = encrypt_decrypt(plaintext, k1, k2, k3, k4, k5)
    # Display the result
    print("Encrypted text:", cipher_result)

elif(choice==2):
    cipher_text = input("Enter the ciphertext: ").replace(" ", "").lower()  # Removing spaces and converting to lowercase
    plaintext_result = encrypt_decrypt(cipher_text, k1, k2, k3, k4, k5)
    # Display the result
    print("Encrypted text:", plaintext_result)




