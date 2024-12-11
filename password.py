# Encryption function
def encrypt(plaintext, key, modulus):
    ciphertext = []
    for char in plaintext:
        # Perform modular addition with the key and modulus
        encrypted_char = (ord(char) + key) % modulus
        # Append the encrypted character to the ciphertext
        ciphertext.append(encrypted_char)
    # Convert the list of integers back to a string
    return ''.join(map(chr, ciphertext))

# Decryption function
def decrypt(ciphertext, key, modulus):
    plaintext = []
    for char in ciphertext:
        # Perform modular subtraction with the key and modulus
        decrypted_char = (ord(char) - key) % modulus
        # Append the decrypted character to the plaintext
        plaintext.append(decrypted_char)
    # Convert the list of integers back to a string
    return ''.join(map(chr, plaintext))

while True:
    choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
    if choice == 'e':
        message = str(input('Input: '))
        encryption_key = 7
        modulus_value = 128
        encrypted_message = encrypt(message, encryption_key, modulus_value)
        print("Encrypted:", encrypted_message)
    elif choice == 'd':
        message = str(input('Output: '))
        encryption_key = 7
        modulus_value = 128
        decrypted_message = decrypt(message, encryption_key, modulus_value)
        print("Decrypted:", decrypted_message)
    elif choice == 'q':
        break  # Exit the loop and end the program
    else:
        print("Invalid choice. Please enter 'e', 'd', or 'q'.")
