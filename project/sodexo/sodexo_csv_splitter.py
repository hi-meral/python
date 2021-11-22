import csv
import os

maxInt = 999999
csv.field_size_limit(maxInt)


def write_new_csv(csv_file_write, column_headers, split_number):

    writer = csv.DictWriter(csv_file_write, fieldnames=column_headers)
    writer.writeheader()

    return writer


def loop_through_csv(fileName, dest_path, csv, split_threshold, column_headers):

    row_counter = 0
    split_number = 0
    write_csv = None

    for row in csv:

        if (row_counter == 0) or (row_counter == split_threshold):

            # close file if it already exists before writing to a new csv file
            if write_csv:
                write_csv.close()

            split_number += 1
            write_csv = open(
                f'{dest_path}/{fileName}_{split_number}.csv', 'w', newline='')
            writer = write_new_csv(write_csv, column_headers, split_number)
            try:
                writer.writerow(row)
            except:
                continue

            row_counter = 0
        else:
            try:
                writer.writerow(row)
            except:
                continue

        row_counter += 1


def main():

    # grab inputs from user
    csv_file_path = input('CSV PATH: ')
    dest_path = input('Enter destination folder: ')
    fileName = input('Input Splitted File Name: ')
    split_threshold = int(input('Rows Per CSV: '))

    with open(csv_file_path, 'r', errors='ignore') as csv_file:
        csv_reader = csv.DictReader(x.replace('\0', '') for x in csv_file)
        column_headers = csv_reader.fieldnames
        loop_through_csv(fileName, dest_path, csv_reader,
                         split_threshold, column_headers)


if __name__ == "__main__":
    main()
