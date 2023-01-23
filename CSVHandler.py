import csv


class CSVHandler:

    @staticmethod
    def write_csv_file(data):
        header = ["user", "level", "score"]

        with open("./data.csv", "a") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writerow(data)
            f.close()

    @staticmethod
    def get_all_rows(value):
        all_data = []
        with open("data.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_data.append(row[value])
            f.close()

        return all_data

    
    @staticmethod
    def get_all_data():
        all_data = []
        with open("data.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_data.append(row)
            f.close()

        return all_data


    @staticmethod
    def delete_all_row(row_to_delete):
        all_data = CSVHandler.get_all_data()
        new_data = []
        for i in range(len(all_data)):
           if all_data[i]["user"] != row_to_delete:
               new_data.append(all_data[i])
            
        header = ["user", "level", "score"]

        with open("data.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(new_data)
            f.close()

    @staticmethod
    def get_all_data_by_row(level, value):
        data = []

        with open("./data.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                if row["user"] == value and row["level"] == str(level):
                    data.append(row)
            f.close()

        return data