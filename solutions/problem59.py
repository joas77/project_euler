# https://projecteuler.net/problem=59

if __name__ == "__main__":
    cipher_file = open("files/p059_cipher.txt")
    cipher_data = cipher_file.read()
    cipher_data =  [int(byte) for byte in cipher_data.split(",")]
    cipher_file.close()
    
    histogram = {}
    
    for i in cipher_data:
        if i in histogram:
            histogram[i] +=1
        else:
            histogram[i] = 1

    print(histogram)