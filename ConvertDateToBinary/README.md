# 3280. Convert Date to Binary

## Built-in Functions

```python
def convertDateToBinary(date: str) -> str:
    split_date = date.split("-")
    # year, month, day = date[0:4], date[5:7], date[8:10]
    result = []
    for num in split_date:
        result.append(bin(int(num))[2:])
    return "-".join(result)
```

In this code we split the given date by "-" but we could also extract the dates directily using slicing since the format does not change. After that we use built-in function `bin()` to convert the date to binary and removing the first two characters since they dont represent the binary value that we want. We are also using a list to store the results since its better than using string concatenation and then joining the results at the end.

```java
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
```

In this solution we are again using built-in functions, this time the Integer class to convert the string to a binary and parsing the date to integer. We also use StringBuilder to store the results since it is more efficient than using string concatenation.

## Convert manually

Math explanation: to convert a number to binary we need to store the remainder of the number at the beggining of the string, the remainder will give us 1 or 0, after that we divide the number by 2, that will give us the next number to convert, we repeat this process until the number is 0.

Example:

```plaintext
10 % 2 = 0 -> 0
10 // 2 = 5
5 % 2 = 1 -> 10
5 // 2 = 2
2 % 2 = 0 -> 010
2 // 2 = 1
1 % 2 = 1 -> 1010
1 // 2 = 0
result = 1010
```

Python code:

```python
def convertDateToBinary(date: str) -> str:
    split_date = date.split("-")
    result = []
    for num in split_date:
        binary = ""
        while int(num) > 0:
            binary = str(int(num) % 2) + binary
            num = int(num) // 2
        result.append(binary)
    return "-".join(result)
```

Java code:

```java
public String convertDateToBinary(String date) {
    String[] split_date = date.split("-");
    StringBuilder result = new StringBuilder();
    for (String string : split_date) {
        Integer number = Integer.parseInt(string);
        StringBuilder bin_number = new StringBuilder();
        while (number > 0) {
            bin_number.insert(0, number % 2);
            number = number / 2;
        }
        result.append(bin_number);
    }
    result.deleteCharAt(result.length() - 1);
    return result.toString();
}
```

You could also create a helper function to convert the passing number to binary, that way you would not need to delete the last character of the result.
