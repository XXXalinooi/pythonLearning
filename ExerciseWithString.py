from datetime import date
import calendar


def exercise_1(input_string):
    result = input_string.split(" ")
    return result


def exercise_2(input_string):
    return input_string.find("Python")


def exercise_3(input_string):
    result = input_string.split("@")
    return result[1]


def exercise_4(input_string):
    if "Python" in input_string:
        return True


def exercise_5(input_string):
    return input_string.count("Python")


def exercise_6(input_list):
    result = list(filter(lambda word: word[0] != 'P', input_list))
    return result


def exercise_7(input_array):
    return list(dict.fromkeys(input_array))


def exercise_8(input_array):
    to_upper = input_array.upper()
    result = to_upper.split(" ")
    return result


def exercise_9(input_string):
    to_array = input_string.split(" ")
    new_list = []
    for i in range(len(to_array)):
        new_list.append(to_array[i][0])
    return new_list


def exercise_10(input_array):
    result = []
    for i in range(len(input_array)):
        result.append(input_array[i].lower().capitalize())
    return result


def exercise_11(input_string, text_to_find, text_to_replace):
    return input_string.replace(text_to_find, text_to_replace)


def exercise_12(input_string):
    return input_string[-2] + input_string[-1]


def exercise_13(input_string):
    return input_string.count("o")


def exercise_14():
    return "Today is " + calendar.day_name[date.today().weekday()] + ", " + date.today().strftime("%d %B %Y") + " year"


def exercise_15(input_list):
    return tuple(input_list)


if __name__ == '__main__':
    print(exercise_3("silly_email@gmail.com"))
