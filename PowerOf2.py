def is_number_power_of_2_first_way(number):
    while number % 2 == 0:
        number = number / 2
    return number == 1


def is_number_power_of_2_second_way(number):
    return (number & number - 1) == 0


if __name__ == '__main__':
    print(is_number_power_of_2_first_way(10))
    print(is_number_power_of_2_first_way(16))
    print(is_number_power_of_2_first_way(2))
    print(is_number_power_of_2_second_way(32))
    print(is_number_power_of_2_second_way(24))
    print(is_number_power_of_2_second_way(1))
