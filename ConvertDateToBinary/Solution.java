class Solution {
    public String convertDateToBinary(String date) {
        String[] split_date = date.split("-");
        StringBuilder result = new StringBuilder();
        result.append(Integer.toBinaryString(Integer.parseInt(split_date[0])));
        result.append("-");
        result.append(Integer.toBinaryString(Integer.parseInt(split_date[1])));
        result.append("-");
        result.append(Integer.toBinaryString(Integer.parseInt(split_date[2])));
        return result.toString();
    }
}