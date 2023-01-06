import csv


class CSVHandler:

    @staticmethod
    def write_csv_file(data):
        header = ["user", "score"]

        with open("data.csv", "a") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writerow(data)
            f.close()

    @staticmethod
    def read_all_data():
        all_data = []
        with open("data.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_data.append(row["user"])

        return all_data
