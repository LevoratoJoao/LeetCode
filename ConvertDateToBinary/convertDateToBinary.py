def convertDateToBinary(date: str) -> str:
    split_date = date.split("-")
    # year, month, day = date[0:4], date[5:7], date[8:10]
    result = []
    for num in split_date:
        result.append(bin(int(num))[2:])
    return "-".join(result)

print(convertDateToBinary("2020-01-10")) # 11111100100-1-1