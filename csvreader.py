###Version by Maverick.php###

import os
import csv

# folder path containing csv files
folder_path = "/path/to/csv/folder"

# output csv file path
output_file_path = "/path/to/output/ExampleDataset/file.csv"

# initialize an empty list to store pos column data
pos_data = []

# loop through each csv file in the folder path
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        csv_file_path = os.path.join(folder_path, filename)
        
        # open the csv file
        with open(csv_file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # loop through each row and extract data from the pos column
            for row in csv_reader:
                # remove spaces from the pos data
                pos_data.append(row["pos"].replace(" ", ""))
                
# write the pos column data to a new csv file without spaces
with open(output_file_path, "w", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["pos"])
    
    for data in pos_data:
        csv_writer.writerow([data])
