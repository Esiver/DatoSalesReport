import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import datetime
print('........')
sales_data = pd.read_csv(r'clean_data.csv',  sep='\t')#, sep='\t'
print('--------')
print(sales_data['date'])
print('--------')
print(sales_data.columns)
print('--------')
print('--------')
#sales_data.columns['date','units','sales','spend','Acos','CPC']
print(sales_data.columns)
sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce') #make a 'date'-column in datetime format
print('xxxxxxxx')
import weekgroup, daygroup, pdfMaker#, write_html, dftopdf

#def main(datafile):
#    week = weekgroup.main(datafile) #Data by week
day = daygroup.main(sales_data) #day data

def week(datafile):
    week = weekgroup.main(datafile) #Data by week
    week_stats = weekgroup.stats(week) #dive into the stats for week    
    weekgroup.makeCsv(week) #make csv file with week dataframe
    weekgroup.plot(week, week_stats) #make plot, saves a file but doesn't plt.plot()
    #weekgroup.makeReport() #make a report in .pdf

week(sales_data)
#main(sales_data)

#week_stats = weekgroup.stats(week) #dive into the stats for week
day_stats = daygroup.stats(day) #... and for days

#weekgroup.makeCsv(week) #make csv file with week dataframe
daygroup.makeCsv(day) #csv for day dataframe

#weekgroup.plot(week, week_stats) #make plot, saves a file but doesn't plt.plot()
daygroup.plot(day, day_stats) #make plot for days(-data)

#weekgroup.makeReport() #make a report in .pdf
daygroup.makeReport() #report in .pdf

def formatMain(mainFile):
    csv_df = mainFile.to_csv()
    mainFile.to_csv(r'all_data.csv')
    print('formatted main data')
    return csv_df


formatMain(sales_data) #format my original data into a dataframe friendly csv
print(formatMain(sales_data))
files_to_read = ['week_max5.csv','week_min5.csv','all_data.csv']

pdfMaker.reporter(files_to_read)

#weekgroup.reporter(files_to_read)