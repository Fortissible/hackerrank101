def countApplesAndOranges(s, t, a, b, apples: list, oranges: list):
    apples.sort(reverse=True)
    oranges.sort()
    print(apples, oranges)
    filtered_apples = filter(lambda apple: apple + a >= s and apple + a <= t, apples)
    filtered_orange = filter(lambda orange: b + orange <= t and b + orange >= s, oranges)
    print(len(list(filtered_apples)))
    print(len(list(filtered_orange)))

if __name__ == '__main__':
    countApplesAndOranges(7,11,5,15, [-2,2,1], [5,-6])
    # first_multiple_input = input().rstrip().split()

    # s = int(first_multiple_input[0])

    # t = int(first_multiple_input[1])

    # second_multiple_input = input().rstrip().split()

    # a = int(second_multiple_input[0])

    # b = int(second_multiple_input[1])

    # third_multiple_input = input().rstrip().split()

    # m = int(third_multiple_input[0])

    # n = int(third_multiple_input[1])

    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))

    # countApplesAndOranges(s, t, a, b, apples, oranges)