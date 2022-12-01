def get_calorie():
    file1 = open('calories.txt', 'r')
    elves = []

    count = 0
    elves.append(0)
    for line in file1.readlines():
        if line != "\n":
            elves[count] += int(line)
        else:
            elves.append(0)
            count += 1

    return elves


def topn(array, n):
    array.sort()
    return sum(array[-n:])


if __name__ == '__main__':
    print(max(get_calorie()))
    print(topn(get_calorie(), 3))
