def commandrunner():
    file = open("filesystem.txt", "r")
    folders = {", /": 0}

    current = ""
    for line in file.readlines():
        if line[0] == "$":
            if "cd .." in line:
                current = current.rsplit(',', 1)[0]
            elif "cd" in line:
                current += ", " + line.split("cd", 1)[1].strip()

        elif "dir" in line:
            folders.setdefault(current + ", " + line.split()[1].strip(), 0)
        else:
            folders[current] += int(line.split()[0].strip())

    add_parents(folders)
    return folders


def add_parents(folders):
    items = sorted(folders.items(), key=lambda k: (len(k[0])), reverse=True)
    for item in items:
        if item[0] != ", /":
            folders[item[0].rsplit(',', 1)[0]] += folders[item[0]]


def get100000orless(folders):
    vals = [values for key, values in folders.items() if 100000 > values]
    return vals


def get_to_be_removed(folders):
    filtered = {k: v for k, v in folders.items() if v > folders.get(", /") - 40000000}
    res_key, res_val = min(filtered.items(), key=lambda x: abs(filtered.get(", /") - 40000000 - x[1]))
    return res_val


if __name__ == '__main__':
    print(sum(get100000orless(commandrunner())))
    print(get_to_be_removed(commandrunner()))
