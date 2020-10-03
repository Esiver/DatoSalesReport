import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import datetime

#get local dependencies
import weekgroup, daygroup#, write_html, dftopdf

sales_data = pd.read_csv(r'clean_data.csv', engine='c', sep='\t')
sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce') #make a 'date'-column in datetime format

week = weekgroup.main() #Data by week
day = daygroup.main() #day data

week_stats = weekgroup.stats(week) #dive into the stats for week
day_stats = daygroup.stats(day) #... and for days

weekgroup.makeCsv(week) #make csv file with week dataframe
daygroup.makeCsv(day) #csv for day dataframe

weekgroup.plot(week, week_stats) #make plot, saves a file but doesn't plt.plot()
daygroup.plot(day, day_stats) #make plot for days(-data)

#weekgroup.makeReport() #make a report in .pdf
#daygroup.makeReport() #report in .pdf

files_to_read = ['week_max5.csv','week_min5.csv', 'clean_data.csv']
weekgroup.reporter(files_to_read)