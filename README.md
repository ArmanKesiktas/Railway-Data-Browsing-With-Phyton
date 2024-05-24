# Railway Data Analysis

This project contains a Python script for analyzing railway data. The script reads `railway.csv` and `railway_data_dictionary.csv` files located on the user's desktop and analyzes the data contained within these files.

## Usage

1. Run the script using the following command:

```bash
python railway_analysis.py
```

2. When the script runs, it will display the first few rows of both `railway.csv` and `railway_data_dictionary.csv`.
3. The script will also print the column names and data types of the `railway.csv` file.
4. The script will then prompt the user to press any key to exit.

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
