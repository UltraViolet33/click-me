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

    
    @staticmethod
    def get_all_data():
        all_data = []
        with open("data.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_data.append(row)

        return all_data


    @staticmethod
    def delete_all_row(row_to_delete):
        all_data = CSVHandler.get_all_data()
        # print(all_data)
        new_data = []
        for i in range(len(all_data)):
           if all_data[i]["user"] != row_to_delete:
            #    all_data.remove(all_data[i])
               new_data.append(all_data[i])
            
        header = ["user", "score"]
        print(new_data)

        with open("data.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(new_data)
            f.close()

