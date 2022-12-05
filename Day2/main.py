import csv


def match_hand():
    with open('rockpapercissors.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        pointsa = {"A": 0, "B": 1, "C": 2}
        pointsx = ["X", "Y", "Z"]
        result = [row for row in reader]
        for row in result:
            if row[1] == 'X':
                row[1] = pointsx[pointsa.get(row[0]) - 1]
            elif row[1] == 'Y':
                row[1] = pointsx[pointsa.get(row[0])]
            else:
                index = pointsa.get(row[0]) + 1 if pointsa.get(row[0]) + 1 < 3 else 0
                row[1] = pointsx[index]
        return result


def calculate_rows(reader):
    score = 0
    points = {"X": 1, "Y": 2, "Z": 3}

    for row in reader:
        matchup = (ord(row[1]) - 64) - (ord(row[0]) - 64)
        result = 3 if matchup == 23 else 0
        if result == 0:
            result = 0 if matchup == 22 or matchup == 25 else 6
        result += points.get(row[1])
        score += result

    return score


if __name__ == '__main__':
    with open('rockpapercissors.csv', newline='') as csvfile:
        read = csv.reader(csvfile, delimiter=' ', quotechar='|')
        print(calculate_rows(read))
    print(calculate_rows(match_hand()))
