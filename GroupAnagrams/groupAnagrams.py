from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    if len(strs) == 1:
        return [strs]

    hash_words = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            # ord('b') - ord('a') = 1 e.g: a=80 and b = 81
            count[ord(c) - ord('a')] += 1

        # Convert count to a tuple since a list can not be a key
        hash_words[tuple(count)].append(s)

    return list(hash_words.values())