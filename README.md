# Railway Data Analysis

This project contains a Python script for analyzing railway data. The script reads `railway.csv` and `railway_data_dictionary.csv` files located on the user's desktop and analyzes the data contained within these files.

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone this repository to your computer or download it as a ZIP file and extract it.
2. Place the `railway.csv` and `railway_data_dictionary.csv` files on your desktop.
3. Install the required Python libraries by running the following command:

```bash
pip install pandas
```

## Usage

1. Run the script using the following command:

```bash
python railway_analysis.py
```

2. When the script runs, it will display the first few rows of both `railway.csv` and `railway_data_dictionary.csv`.
3. The script will also print the column names and data types of the `railway.csv` file.
4. The script will then prompt the user to press any key to exit.

### Script Details

The script performs the following steps:

1. Reads the `railway.csv` and `railway_data_dictionary.csv` files from the user's desktop.
2. Displays the first few rows of `railway.csv` and `railway_data_dictionary.csv`.
3. Prints the column names and data types of `railway.csv`.
4. Prompts the user to press any key to exit the script.

### Example Output

**railway.csv FIRST FEW ROWS**

```
    Column1    Column2    Column3
0   value1     value2     value3
1   value4     value5     value6
2   value7     value8     value9
```

**railway_data_dictionary.csv FIRST FEW ROWS**

```
    Column1    Description
0   Column1    Explanation1
1   Column2    Explanation2
2   Column3    Explanation3
```

**railway.csv Column Names and Data Types**

```
Column1    object
Column2    object
Column3    int64
dtype: object
```
