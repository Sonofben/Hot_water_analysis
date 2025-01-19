                                                              **Documentation**

**Overview**
This project analyzes hot water consumption data from multiple Excel files, specifically focusing on the Covid-19 period. The analysis calculates total and average daily consumption and visualizes the consumption trends using matplotlib.

**Features**
- Read and process multiple Excel files containing hot water consumption data.
- Filter data for the Covid-19 period.
- Calculate total and average daily hot water consumption during the Covid-19 period.
- Visualize hot water consumption trends.

**Requirements**
pandas
matplotlib
glob

**Installation**
You can install the required packages using pip:
pip install pandas matplotlib

**Usage**
Place your Excel files in a directory and update the file path in the script. Then, run the script to analyze the data and generate visualizations.
python analyze_hot_water.py

**Code Description**
**1 analyze_hot_water_data:** Reads the data, cleans it, filters for the Covid-19 period, and calculates consumption statistics.
**2 Main Script:** Uses glob to read multiple Excel files, aggregates the data, calculates overall statistics, and generates visualizations.

**Output**
**Total Hot Water Consumption:** Total consumption during the Covid-19 period across all files.
**Average Daily Hot Water Consumption:** Average daily consumption during the Covid-19 period across all files.
**Visualization:** A time series plot of hot water consumption during the Covid-19 period.
