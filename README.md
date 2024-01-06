## Clock V Scheme 
### designed for ENIGMA (An Information Security Competition)

### Overview of the Scheme:
The code defines a function encrypt_decrypt that takes a plaintext and keys (k1 to k5) as input and performs encryption or decryption based on user choice. The encryption process involves dividing the plaintext into chunks of 4 characters, mapping characters to their corresponding integer values, and applying the specified operations for each character in the chunk. The main program takes user input for encryption or decryption, keys, and plaintext or ciphertext.

### Encryption Process:
For each character in a 4-character chunk:
1) Multiply k3 with k1 for the first character, k3 with k2 for the second character, k3 with k5 for the third character, and k3 with k4 for the fourth character.
2) Subtract the character value (mapped from 'a' to 0) from the result.
3) If the result is negative, adjust it to a positive value.
4) Apply modulo 26 to keep the result within the alphabet range.
5) Map the result back to characters ('a' to 'z').
