import csv

def main():
    with open('groundtruth/via_project_2Mar2021_16h56m.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                row_id = int(row[2])
                x = int(row[2])
                y = int(row[2])
                width = int(row[2])
                height = int(row[2])
                print(x,y,width,height)

            line_count += 1


if __name__ == '__main__':
    main()