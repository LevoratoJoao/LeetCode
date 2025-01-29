function isPrefixOfWord(sentence: string, searchWord: string): number {
    let splitStr: string[] = sentence.split(" ");
    for (let i = 0; i < splitStr.length; i++) {
        if (splitStr[i].startsWith(searchWord)) {
            return i + 1;
        }

    }
    return -1;
};