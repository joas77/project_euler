# https://projecteuler.net/problem=63

if __name__ == "__main__":
    
    powerful_digits = []

    for i in range(1, 10):
        for j in range(1,100):
            if len(str(i**j)) == j:
                powerful_digits.append((i,j))

    print(powerful_digits)
    print(f"solution = {len(powerful_digits)}")