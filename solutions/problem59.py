# https://projecteuler.net/problem=59

def xor(a, b):
    return a^b

if __name__ == "__main__":
    cipher_file = open("files/p059_cipher.txt")
    cipher_data = cipher_file.read()
    cipher_data =  [int(byte) for byte in cipher_data.split(",")]
    cipher_file.close()

    lower_chars = range(ord('a'), ord('z') + 1)
    printable_chars = range(32, 127)

    for c in lower_chars:
        for i in range(3):
            decoded_data = [chr(xor(c, d)) for d in cipher_data[i::3]]
            if all(d.isprintable() for d in decoded_data):
                print(f"{chr(c)} could be part of password in  position {i}")
                print([chr(xor(c, d)) for d in cipher_data[i::3]])

    # after some manual analisis it's easy to find oout the password
    password = 'exp'

    # decoding the secret message
    print("="*48)

    secret_msg = ""
    for i in range(0, len(cipher_data), 3):
        secret_msg +=  "".join(chr(xor(ord(p), d)) for p, d in zip(password, cipher_data[i:i+3]))

    print(secret_msg)
    print("="*48)
    print("solution (sum of ascii values of secret message):")
    print(sum(ord(c) for c in secret_msg))
