#highs_lows
import csv  # Importing the csv module for reading CSV files
from matplotlib import pyplot as plt  # Importing pyplot module from matplotlib for plotting
from datetime import datetime  # Importing datetime module for working with dates and times

# Path to the CSV file containing weather data
file_path = r'C:\Users\19548\OneDrive\Desktop\python excerise\sitka_weather_2014.csv'

# Open the CSV file and read its contents
with open(file_path) as f:
    reader = csv.reader(f)  # Create a reader object
    header_row = next(reader)  # Get the header row
    print(header_row)  # Print the header row

    # Initialize lists to store dates, high temperatures, and low temperatures
    dates, highs, lows= [], [], []
    
    # Loop through each row in the CSV file
    for row in reader: 
        try:
            # Convert the date string to a datetime object
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            # Convert the high temperature string to an integer
            high = int(row[1])
            # Convert the low temperature string to an integer
            low = int(row[3])
        except ValueError:
            # Handle the case where there might be missing values
            print(current_date, 'missing Value')
        else:
            # Append the current date, high, and low temperatures to their respective lists
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Create a figure object for the plot
fig = plt.figure(dpi=128, figsize=(10, 6))

# Plot dates against highs
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Setup graph title and axis labels
plt.title("Daily highs and lows temperatures 2014", fontsize=24)
plt.xlabel('Date', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Rotate x-axis labels for better readability
fig.autofmt_xdate()

# Display the plot
plt.show()

