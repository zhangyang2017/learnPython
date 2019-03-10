import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    """
    The csv module contains a next() function, which returns the next line in the file when passed the reader object. 
    In the preceding listing we call next() only once so we get the first line of the file, which contains the file headers
    """

   # for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    ## use enumerate() on the list to get the index of each item, as well as the value.

    # get high temps from file
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plotting data in a temperature chart

fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# format plot
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize = 20)
plt.xlabel('', fontsize=16)

# draws the date labels diagonally to prevent overlapping
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
