import csv


def initialize():
    with open('initialize.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        result = [row for row in reader]

    stacks = [[], [], [], [], [], [], [], [], []]
    for i in range(7, -1, -1):
        for j in range(0, len(result[i]), 1):
            if not result[i][j].isspace():
                stacks[j].append(result[i][j])
    return stacks


def from_to(stacks):
    file1 = open('stacks.txt', 'r')
    for line in file1.readlines():
        digits = [int(s) for s in line.split() if s.isdigit()]
        for i in range(0, digits[0], 1):
            item = stacks[digits[1] - 1].pop()
            stacks[digits[2] - 1].append(item)
    return stacks


def cratemover_9001(stacks):
    file1 = open('stacks.txt', 'r')
    for line in file1.readlines():
        digits = [int(s) for s in line.split() if s.isdigit()]

        items = stacks[digits[1] - 1][-digits[0]:]
        del stacks[digits[1] - 1][-digits[0]:]
        stacks[digits[2] - 1].extend(items)

    return stacks


def get_top(stacks):
    top = ""
    for row in stacks:
        top += row.pop()
    return top


if __name__ == '__main__':
    stack = initialize()
    stonk = from_to(stack)
    stack2 = initialize()
    stonk2 = cratemover_9001(stack2)
    print(get_top(stonk))
    print(get_top(stonk2))
