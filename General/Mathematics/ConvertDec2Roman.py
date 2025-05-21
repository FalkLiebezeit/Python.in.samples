# this program converts decimal numbers tro roman

def decimal_to_roman(num):
    # Definition der römischen Zahlensymbole und ihrer Werte
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = ""

    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value
    return result

# Beispiel für die Nutzung
decimal_number = 1987
roman_number = decimal_to_roman(decimal_number)
print(f"{decimal_number} in römischen Zahlen ist: {roman_number}")
