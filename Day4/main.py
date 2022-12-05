import csv


def read_pairs():
    with open('cleaning_pairs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        result = [row for row in reader]

    full = 0
    overlap = 0
    for row in result:
        numbers = [int(s) for s in row[0].split("-") if s.isdigit()]
        numbers2 = [int(s) for s in row[1].split("-") if s.isdigit()]

        full += 1 if calc_full_overlap(numbers, numbers2) else 0
        overlap += 1 if calc_overlap(numbers, numbers2) else 0

    return full, overlap


def compare_int(integer, integer2):
    if integer > integer2:
        return 1
    elif integer < integer2:
        return -1
    return 0


def calc_full_overlap(numbers, numbers2):
    comp1 = compare_int(numbers[0], numbers2[0])
    comp2 = compare_int(numbers[1], numbers2[1])

    if (comp1 > 0) is not (comp2 > 0):
        return True
    elif (comp1 == -1) is not (comp2 == -1):
        return True
    elif (comp1 == 0) and (comp2 == 0):
        return True
    return False


def calc_overlap(numbers, numbers2):
    if numbers2[0] <= numbers[1] <= numbers2[1]:
        return True
    elif numbers[0] <= numbers2[1] <= numbers[1]:
        return True
    return False


if __name__ == '__main__':
    print(read_pairs())
