# Найти максимальную цифру числа


def get_max_digit(number):
    # 0....9
    number *= -1 if number < 0 else 1
    max_digit = 0
    # min = 9

    while number > 0:
        digit = number % 10

        if digit == 9:
            max_digit = 9
            break

        if digit > max_digit:
            max_digit = digit
        number //= 10

    return max_digit


def main():
    number = int(input("Please input your number:  "))
    max_digit = get_max_digit(number)

    msg = f"Max digit in {number} is {max_digit} "
    print(msg)

main()
