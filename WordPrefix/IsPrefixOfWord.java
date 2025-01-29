class Dukwon {
    public static int isPrefixOfWord(String sentence, String searchWord) {
        String[] splitStr = sentence.split(" ");
        for (int i = 0; i < splitStr.length; i++) {
            if (splitStr[i].startsWith(searchWord)) {
                return i + 1;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        System.out.println(isPrefixOfWord("i love eating burger", "burg"));
    }
}