# license: MIT
# source https://www.youtube.com/watch?v=tG8PPne7ef0
# This is python script
# take Roman number as input and convert it to decimal number
# create a dictionary with Roman number and decimal number

ROMANS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# create a function to convert Roman number to decimal number
def roman_to_decimal(roman):
    result = 0
    for i in range(len(roman)):
        if i > 0 and ROMANS[roman[i]] > ROMANS[roman[i - 1]]:
            result += ROMANS[roman[i]] - 2 * ROMANS[roman[i - 1]]
        else:
            result += ROMANS[roman[i]]
    return result


# create function that takes input from user
def main():
    roman = input('Enter a Roman numeral: ')
    print('The decimal number is', roman_to_decimal(roman))
    # call the function
main()













# create a test case
def test_roman_to_decimal():
    assert roman_to_decimal('I') == 1
    assert roman_to_decimal('V') == 5
    assert roman_to_decimal('X') == 10
    assert roman_to_decimal('L') == 50
    assert roman_to_decimal('C') == 100
    assert roman_to_decimal('D') == 500
    assert roman_to_decimal('M') == 1000
    assert roman_to_decimal('II') == 2
    assert roman_to_decimal('III') == 3
    assert roman_to_decimal('IV') == 4
    assert roman_to_decimal('VI') == 6
    assert roman_to_decimal('VII') == 7
    assert roman_to_decimal('VIII') == 8
    assert roman_to_decimal('IX') == 9
    assert roman_to_decimal('XII') == 12
    assert roman_to_decimal('XIII') == 13
    assert roman_to_decimal('XIV') == 14
    assert roman_to_decimal('XVI') == 16
    assert roman_to_decimal('XVII') == 17
    assert roman_to_decimal('XVIII') == 18
    assert roman_to_decimal('XIX') == 19
    assert roman_to_decimal('XX') == 20
    assert roman_to_decimal('XXI') == 21
    assert roman_to_decimal('XXII') == 22
    assert roman_to_decimal('XXIII') == 23
    assert roman_to_decimal('XXIV') == 24
    assert roman_to_decimal('XXV') == 25
    assert roman_to_decimal('XXVI') == 26
    assert roman_to_decimal('XXVII') == 27
    assert roman_to_decimal('XXVIII') == 28
    assert roman_to_decimal('XXIX') == 29
    assert roman_to_decimal('XXX') == 30
    assert roman_to_decimal('XXXI') == 31
    assert roman_to_decimal('XXXII') == 32
    assert roman_to_decimal('XXXIII') == 33
    assert roman_to_decimal('XXXIV') == 34
    assert roman_to_decimal('XXXV') == 35
    assert roman_to_decimal('XXXVI') == 36
    assert roman_to_decimal('XXXVII') == 37

# call the test case
test_roman_to_decimal()
