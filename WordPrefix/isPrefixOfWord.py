def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split(" ")
    for i, word in enumerate(words):
        if word.startswith(searchWord):
            return i + 1
    return -1

print(isPrefixOfWord("i love eating burger", "burg"))