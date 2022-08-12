from helper import generate_random_list


def main():

    ls = generate_random_list(10000, 10000, 900000)
    print(*ls)


main()
