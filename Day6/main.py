def all_unique(iterable):
    return len(set(iterable)) == len(iterable)


def first_start_of_packet(nr_unique):
    file = open("stream.txt", "r")

    count = 0
    chars = []
    for char in file.readlines()[0]:
        chars.append(char)
        count += 1
        if len(chars) > nr_unique - 1:
            if all_unique(chars):
                return count
            chars.pop(0)
    return -1


if __name__ == '__main__':
    print(first_start_of_packet(4))
    print(first_start_of_packet(14))
