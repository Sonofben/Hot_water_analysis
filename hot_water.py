import pandas as pd
import matplotlib.pyplot as plt
import glob

def analyze_hot_water_data(data):
    data.dropna(subset=['Meter Reading Date', 'Water'], inplace=True)
    try:
        data['Water'] = pd.to_numeric(data['Water'])
    except ValueError:
        print("Error converting 'Water' column to numeric. Check data format.")
    
    covid_start_date = '2020-03-01'
    covid_end_date = '2021-12-31'
    
    covid_data = data[(data['Meter Reading Date'] >= covid_start_date) & (data['Meter Reading Date'] <= covid_end_date)]
    
    total_consumption = covid_data['Water'].sum()
    average_daily_consumption = total_consumption / len(covid_data)
    
    return total_consumption, average_daily_consumption, covid_data

file_paths = glob.glob('path/to/*.xlsx')

total_consumption_all = 0
average_daily_consumption_all = 0
all_covid_data = pd.DataFrame()

all_data = pd.concat([pd.read_excel(f) for f in file_paths])

total_consumption, average_daily_consumption, covid_data = analyze_hot_water_data(all_data)

total_consumption_all += total_consumption
average_daily_consumption_all += average_daily_consumption
all_covid_data = pd.concat([all_covid_data, covid_data])

print("Total Hot Water Consumption (All Files, Covid Period):", total_consumption_all)
print("Average Daily Hot Water Consumption (All Files, Covid Period):", average_daily_consumption_all)

plt.figure(figsize=(10, 6))
plt.plot(all_covid_data['Meter Reading Date'], all_covid_data['Water'])
plt.xlabel('Date')
plt.ylabel('Hot Water Consumption')
plt.title('Hot Water Consumption During Covid Period (All Files)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
