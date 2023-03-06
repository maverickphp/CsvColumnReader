# CsvColumnReader

<h3>CSV Column Data Extractor</h3>
The CSV Column Data Extractor is a Python program that reads multiple CSV files from a folder, copies data from a column named "pos", and pastes it in a new CSV file without spaces. This program can be used to extract data from a specific column of multiple CSV files and combine them into a single CSV file.

<h4>Requirements</h4>
- Python 3.x
- csv module (comes with Python)

<h4>Installation</h4>

1. Clone the repository or download the ZIP file and extract its contents to a folder on your computer
2. Make sure you have Python 3.x installed on your computer. You can download it from the official website: https://www.python.org/downloads/
3. No additional installation is required for this program

<h4>How to use</h4>

1. Put all the CSV files you want to extract data from in a folder.
2. Open the csvreader.py file in a text editor or VSCode.
3. Modify the folder_path and output_file_path variables in the program to match the folder containing your CSV files and the path and name of the output file you want to create.
4. Run the program by typing python csvreader.py in your terminal or command prompt.
5. The program will extract data from the "NameOfColumn" column of all the CSV files in the folder and combine them into a single CSV file without spaces in the column names.

<h4>Example</h4>
Suppose you have a folder called csv_files containing the following CSV files:
```sh
csv_files/
    file1.csv
    file2.csv
    file3.csv
```

<b><h3>NOTE:</h3></b>
If you have any issue you can open a thread in issues.
Thanks!
