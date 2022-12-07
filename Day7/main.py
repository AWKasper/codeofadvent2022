def commandrunner():
    file = open("filesystem.txt", "r")
    folders = {"/": [0, ""]}

    current = "/"
    for line in file.readlines():
        if line[0] == "$":
            if "cd" in line:
                current = line.split("cd", 1)[1].strip()
            elif "cd .." in line:
                current = folders[current][1]

        elif "dir" in line:
            folders.setdefault(line.split()[1].strip(), [0, current])
        else:
            folders[current][0] += int(line.split()[0].strip())

    add_parents(folders)

    return folders


def add_parents(folders):
    for folder in folders.values():
        add_parent_rec(folder, folders)


def add_parent_rec(folder, folders):
    if folder[1] != "":
        folders[folder[1]][0] += folder[0]
        add_parent_rec(folders[folder[1]], folders)


def get100000orless(folders):
    vals = [values for key, values in folders.items() if 100000 > values[0]]
    keys = [key for key, values in folders.items() if 100000 > values[0]]
    print(keys)
    return vals


if __name__ == '__main__':
    print(get100000orless(commandrunner()))
