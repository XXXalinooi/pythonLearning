def first_index(given_array, number_to_find):
    for i in range(len(given_array) - 1):
        if given_array[i] == number_to_find:
            return i
    else:
        return -1


def last_index(given_array, number_to_find):
    for i in range(len(given_array)-1, 0, -1):
        if given_array[i] == number_to_find:
            return i
    else:
        return -1


def find_first_and_last_occur_of_number(given_array, number_to_find):
    first_result = first_index(given_array, number_to_find)
    if first_result == -1:
        print('-1, -1')
    else:
        print(first_result, last_index(given_array, number_to_find))


if __name__ == '__main__':
    array = [4, 1, 5, 6, 4, 9, 6, 5]
    find_first_and_last_occur_of_number(array, 5)
