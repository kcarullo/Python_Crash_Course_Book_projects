 
import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = ('sitka_weather_2014.csv')
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        
        high = int(row[1])
        highs.append(high)
    
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
# Plot data.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')

#format the plot
plt.title("Daily high temps, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
