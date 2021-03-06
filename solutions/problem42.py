# https://projecteuler.net/problem=42

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
import string
import math

def encode_word(word:str)->int:
    letters = string.ascii_uppercase
    word = word.upper()
    wsum = 0
    for c in word:
        wsum += letters.find(c) + 1

    return wsum

def is_square(n:int)->bool:
    sqrt = int(math.sqrt(n))
    return sqrt*sqrt == n

if __name__ == "__main__":
    words_file =open("files/p042_words.txt")
    data = words_file.read()
    words_file.close()
    
    data = data.replace('"', '')
    words = data.split(",")

    triangle_words_count = 0

    for word in words:
        Tn = encode_word(word)
        if is_square(8*Tn + 1):
            print(Tn, word)
            triangle_words_count += 1

    print(f"solution: {triangle_words_count}")
