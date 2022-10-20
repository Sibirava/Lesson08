# 5! = 5*4*3*2*1

def factorial(number):
    if number < 0:
        return -1
    else:
        f = 1
        for item in range(2, number + 1):
            f *= item

        return f


def main():
    number = int(input("Input your number: "))

    result = factorial(number)

    if result != -1:
        msg = f"{number}! = {result}"
    else:
        msg = "Error! Wrong number, number should be positive or zero."

    print(msg)


main()
