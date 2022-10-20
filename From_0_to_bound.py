# вывсести все значения от 0 до bound

def test(bound):
    # item = 0
    msg = ""
    # while item < bound:
    #     item += 2
    #     msg += str(item) + " "
    # return msg

    for item in range(2, bound + 1, 2):
        msg += item
    return msg


def main():
    s = test(20)
    print(s)


main()
