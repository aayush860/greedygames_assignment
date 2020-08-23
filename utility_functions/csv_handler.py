import csv
class csv_handler:
    def __init__(self):
        self.table = [['Name', 'Number of Reviews', 'Last Date of Update', 'Number of Days', 'Score']]

    def csv_writer(self, new_table):
        file = open('/Users/aayushbhargava/Downloads/g4g.csv', 'w+', newline='')
        with file:
            write = csv.writer(file)
            write.writerows(new_table)