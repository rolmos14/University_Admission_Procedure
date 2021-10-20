word1, word2 = [input() for _ in range(2)]
brand_name = ""
for char1, char2 in zip(word1, word2):
    brand_name += char1 + char2
print(brand_name)
