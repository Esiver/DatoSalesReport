import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import datetime
print('hellooooooo000000000000000000')
#get local dependencies

print('colllllllll')
sales_data = pd.read_csv(r'clean_data_1.csv',engine='c')#, sep='\t'
print('colllllllll')
print(sales_data)
#sales_data.columns = ['date','units','sales','Acos','spend','CPC']
print(sales_data)
sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce') #make a 'date'-column in datetime format
print('0000000000000000000000000')
import weekgroup, daygroup, pdfMaker#, write_html, dftopdf
print('-------------------------------')
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

def formatMain(mainFile):
    csv_df = mainFile.to_csv()
    mainFile.to_csv(r'all_data.csv')
    print('made csv MAIN-----------------------------------')
    return csv_df

formatMain(sales_data) #format my original data into a dataframe friendly csv

files_to_read = ['week_max5.csv','week_min5.csv','all_data.csv']

pdfMaker.reporter(files_to_read)

#weekgroup.reporter(files_to_read)