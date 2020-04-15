
# Using p022_names.txt, a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 x 53 = 49714
# What is the total of all the name scores in the file?

def alph_order_char(character:str)->int:
    c = character.lower()
    return ord(c) - ord("a") + 1

names = []
with open("p022_names.txt") as names_file:
    data = names_file.read()
    data = data.replace('"', '')
    names = data.split(",")
    names.sort()
    assert names[938 - 1] == "COLIN", "names not sorted correctly!"

names_scores = 0

for index, name in enumerate(names, start=1):
    score = 0
    for c in name:
        score += alph_order_char(c)
    names_scores += score*index

print(f"Total name scores: {names_scores}")

