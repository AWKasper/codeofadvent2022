def find_duplicates():
    file1 = open('rucksacks.txt', 'r')
    dups = []
    for line in file1.readlines():
        firstpart, secondpart = line[:len(line) // 2], line[len(line) // 2:]
        dups.extend(find_duplicate_char(firstpart, secondpart))
    return dups


def find_groups():
    file1 = open('rucksacks.txt', 'r')
    lines = file1.readlines()
    dups = []
    for i in range(0, len(lines), 3):
        chars = []
        for char in lines[i].strip():
            if char in lines[i + 1] and char in lines[i + 2] and char not in chars:
                dups.append(char)
                chars.append(char)
    print(len(dups))
    return dups


def find_duplicate_char(part1, part2):
    dups = []
    chars = []
    for char in part1:
        if char in part2 and char not in chars:
            dups.append(char)
            chars.append(char)
    return dups


def calc_score(dups):
    score = 0
    for char in dups:
        score += 26 if char.isupper() else 0
        score += ord(char.lower()) - 96
    return score


if __name__ == '__main__':
    print(calc_score(find_duplicates()))
    print(calc_score(find_groups()))
