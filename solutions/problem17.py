# https://projecteuler.net/problem=17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 
# 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

NUM_WORDS_MAP = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
}

def number_to_word(n:int)->int:
    if 1<=n<20:
        return  NUM_WORDS_MAP[n]
    elif 20<=n<100:
        return f"{NUM_WORDS_MAP[10*(n//10)]} {number_to_word(n%10)}"
    elif 100<=n<1000:
        units = number_to_word(n % 100)
        return f"{number_to_word(n//100)} {NUM_WORDS_MAP[100]} {"and " + units if len(units)>0 else "" }"
    elif n==1000:
        return f"{NUM_WORDS_MAP[1]} {NUM_WORDS_MAP[1000]}"

    return ""

def count_char_word_number(nstr: str) -> int:
    words = nstr.split()
    return sum(len(w) for w in words)

if __name__ == "__main__":
    LIMIT = 1000
    sum_letters = 0

    assert count_char_word_number( number_to_word(115) ) == 20
    assert count_char_word_number( number_to_word(342) ) == 23

    for i in range(1, LIMIT+1):
        number = number_to_word(i)
        sum_letters += count_char_word_number(number)
        print(f"{i} --> {number}")

    print(f"solution: {sum_letters}")
