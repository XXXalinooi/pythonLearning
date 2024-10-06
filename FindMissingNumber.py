def find_missing_number(list_with_numbers):
    sum_with_missing_element = 0
    for i in range(len(list_with_numbers)):
        sum_with_missing_element = sum_with_missing_element + list_with_numbers[i]
    sum_without_missing_number = (2 + len(list_with_numbers)) * (len(list_with_numbers) + 1) / 2
    return sum_without_missing_number - sum_with_missing_element


if __name__ == '__main__':
    numbers = [1, 2, 3, 5]
    numbers2 = [4, 3, 2, 5, 7, 6]
    print(find_missing_number(numbers))
    print(find_missing_number(numbers2))
