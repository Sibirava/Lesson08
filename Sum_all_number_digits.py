

# 12345 -->15
# 1111111111 -->10

def sum_all_number_digits(number):
    # number = abs(number)
    number *= -1 if number < 0 else 1
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s


def main():
    number = int(input("Please input your number:  "))
    s = sum_all_number_digits(number)

    msg = f"Sum of number digits  {number} is {s} "
    print(msg)


main()
