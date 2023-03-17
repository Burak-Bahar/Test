import csv

array = []
array2 = []


def connection():
    with open('C:/Users/hobbits_to_isengard/Desktop/basvuru/country_vaccination_stats.csv') as file:
        read = csv.reader(file)
        for row in read:
            array.append(row)


def find_smallest(c_name):
    num = -1
    for row in array[1:]:
        if row[0] == c_name and row[2] != "":
            if num == -1:
                num = int(row[2])
            if num > int(row[2]):
                num = int(row[2])
    if num == -1:
        num = 0
    return num


def merid():
    dictionary = {

    }
    for row in array[1:]:
        if row[0] not in dictionary:
            dictionary[row[0]] = [int(row[2])]
        else:
            dictionary[row[0]].append(int(row[2]))
    for entry in dictionary.values():
        entry.sort()
        length = len(entry)
        if length % 2 == 0:
            array2.append((entry[int(length / 2)] + entry[int(length / 2) - 1]) / 2)
        else:
            array2.append(entry[int(length / 2)])



if __name__ == "__main__":
    connection()
    for row in array[1:]:
        if row[2] == "":
            name = row[0]
            min_number = find_smallest(name)
            row[2] = str(min_number)

    merid()
