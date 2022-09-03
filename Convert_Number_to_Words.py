def convert_number_to_words(num):
    li_units = (
        "0",
        "thousand",
        "million",
        "billion",
        "trillion",
        "quadrillion",
        "quintillion",
        "hextillion",
        "septillion",
        "octillion",
        "nonillion",
        "decillion",
        "undecillion",
        "duodecillion",
        "tredecillion",
        "quattuordecillion",
        "quindecillion",
        "hexdecillion",
        "septendecillion",
        "octodecillion",
        "novemdecillion",
    )
    li_0_to_9 = (
        "0",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    li_11_to_19 = (
        "0",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    )
    li_10_to_90 = (
        "0",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    )

    starting_index = 0
    whitespace = " "

    result = ""

    while len(num) % 3 != 0:
        num = "0" + num

    for digit in range((len(num) // 3) - 1, -1, -1):
        first_digit = int(num[starting_index])
        second_digit = int(num[starting_index + 1])
        third_digit = int(num[starting_index + 2])

        result += li_0_to_9[first_digit] + whitespace
        if first_digit != 0:
            result += "hundred" + whitespace
        if second_digit == 1 and third_digit != 0:
            result += li_11_to_19[third_digit] + whitespace
        else:
            result += li_10_to_90[second_digit] + whitespace
            result += li_0_to_9[third_digit] + whitespace

        if not (first_digit == 0 and second_digit == 0 and third_digit == 0):
            result += li_units[digit] + whitespace

        starting_index += 3

    li_result = result.strip().split(" ")
    li_result = list(filter(lambda x: x != "0", li_result))

    result = ""

    for word in li_result:
        result += word + " "
    return result
