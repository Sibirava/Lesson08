# s = "pizza"
#
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for item in s:
#     print(item * 3, end= ' ')

def hello(count):
    s = ' '
    for _ in range(count):
        s += "Hello\n"
    return s


def main():
    print(hello(5))


main()
