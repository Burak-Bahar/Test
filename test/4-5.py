import csv

array = []


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


if __name__ == "__main__":
    connection()
    for row in array[1:]:
        if row[2] == "":
            name = row[0]
            min_number = find_smallest(name)
            row[2] = str(min_number)

    for row in array[1:]:
        print(row)
