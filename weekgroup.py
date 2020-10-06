import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import datetime

import csv
from fpdf import FPDF

sales_data = pd.read_csv(r'clean_data.csv', engine='c')#, sep='\t')
sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce') #make a 'date'-column in datetime format

def main():
    
    week_data = sales_data
    week_data['week'] = week_data['date'].dt.week #make week column, just in case...
    week_data = week_data[['units','sales','spend']].groupby(week_data['date'].dt.week).sum().reset_index() #sum columns grouped by date
    week_data['ROI'] = (week_data['sales'] - week_data['spend'])/week_data['spend'] # calculate new ROI column for week df
    week_data['ACOS'] = (week_data['spend']/week_data['sales']) #and calculate ACOS just because....
    
    week_data = week_data.round(3)

    print('----------------------- DATA GROUPED BY WEEK ------------')
    week_data.columns= ['week','units','sales','spend','ROI','ACOS']
    print(week_data)

    return week_data

def makeHtml (df):
    html_df = df.to_html
    print('made html-----------------------------------')
    print(html_df)
    print('made html-----------------------------------')
    return html_df

def makeCsv (df):
    csv_df = df.to_csv
    df.to_csv(r'week_csv.csv')
    print('made csv-----------------------------------')
    return csv_df

#------------------------------------------------------
'''
class PDF(FPDF):
    def header(self):
        self.image('datologo.png',10,10,30,30) #logo
        self.set_font('Arial','B',16) #Arial bold size 16
        self.cell(80) #transform cell 80
        self.cell(30,10,'I am Title',1,0,'C')
        self.ln(50)
    
    def figure(self, mig):
        self.ln(30)
        # Logo
        self.image(mig, 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)
    
    def table(self, dfile):
        self.cell(30,10,dfile)
        self.ln(10)
        self.set_font('Courier','',size=12)
        with open(dfile, newline='') as f:
            data = csv.reader(f)
            th = self.font_size
            page_width = self.w - 2 * self.l_margin
            col_width = page_width/8
            for row in data:
                self.cell(col_width,th,row[0], border=1, align='C')
                self.cell(col_width,th,row[1], border=1,align='C')
                self.cell(col_width,th,row[2], border=1,align='C')
                self.cell(col_width,th,row[3], border=1,align='C')
                self.cell(col_width,th,row[4], border=1,align='C')
                self.cell(col_width,th,row[5], border=1,align='C')

                self.ln(th)
        self.ln(th*2)
    def maker(self,fig,csvfile):
        #self.add_page()
        #self.header()
        #self.figure(fig)
        self.table(csvfile)

#pdf = PDF()
#pdf.add_page()

#pdf.maker('datologo.png','week_max5.csv')
#pdf.maker('datologo.png','week_min5.csv')
#pdf.output('newMan.pdf', 'F')

def reporter(datafile):
    pdf = PDF()
    pdf.add_page()
    for x in datafile:
        pdf.maker('datologo.png',x)
    pdf.output('newMan.pdf', 'F')

#---------------------------------------------------
'''
def stats(x):
    week_sales_max = x.nlargest(5,'sales')
    week_sales_min = x.nsmallest(5,'sales')
    
    #print('HEYYYYYYYYYYYYYYYYY DUDE')
    #print(week_sales_max,week_sales_min)
    #minmax_sales = week_sales_max.merge(week_sales_min, how='outer')

    week_ROI_max = x.nlargest(5,'ROI')
    week_ROI_min = x.nsmallest(5,'ROI')
    mean_week_sales = x['sales'].mean(skipna= True)
    #mean_sales = sales_data['sales'].mean(skipna = True)

    week_sales_min.to_csv(r'week_min5.csv')
    week_sales_max.to_csv(r'week_max5.csv')
    return mean_week_sales

def plot(d, s):
    mean = s
    d.plot(x='week', y=['sales', 'spend'], kind = 'bar')
    plt.axhline(y=s, color='r', linestyle='dotted')
    ax = d['ROI'].plot(secondary_y=True)
    ax.set_ylabel('ROI')
    #plt.show()
    plt.savefig('week_plot.png')

    
