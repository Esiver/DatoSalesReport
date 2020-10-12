import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import datetime

import csv
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image('datologo.png',10,10,30,30) #logo
        self.set_font('Arial','B',16) #Arial bold size 16
        self.cell(80) #transform cell 80
        self.cell(75,10,'Sales Data Report',1,0,'C')
        self.ln(40)
    
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
        self.ln(5)
    
    def execSum():
        print('making executive summary')

    def grapher(self,graph,title):
        print('inserting graph...')
        #self.ln(30)
        # Logo
        self.set_font('Arial', 'B', 15)
        self.cell(150, 10, title, 1, 100, 'C')
        self.image(graph,w=150,h=100)
        self.cell(w=0,ln=2)
        #self.cell(280)
        
        
    def table(self, dfile):
        self.cell(30,10,dfile)
        self.ln(10)
        self.set_font('Courier','',size=12)
        print('I got this far and thats alright')
        with open('clean_data.csv', newline='') as f:
            print('ddddddddddddddddddddddddddddddddddd')
            print(f)
            data = csv.reader(f)
            th = self.font_size
            page_width = self.w - 2 * self.l_margin
            col_width = page_width/8
            
            for row in data:
                for column in row:
                    self.cell(col_width,th,column, border=1, align='C')
                    
                #self.cell(col_width,th,column[row],border=1,align='C')
                #self.cell(col_width,th,row[0], border=1, align='C')
                #self.cell(col_width,th,row[1], border=1,align='C')
                #self.cell(col_width,th,row[2], border=1,align='C')
                #self.cell(col_width,th,row[3], border=1,align='C')
                #self.cell(col_width,th,row[4], border=1,align='C')
                #self.cell(col_width,th,row[5], border=1,align='C')

                self.ln(th)
        self.ln(th*2)
    def maker(self,fig,csvfile):
        #self.add_page()
        #self.header()
        #self.figure(fig)
        #self.grapher(graph)
        self.table(csvfile)


def reporter(datafile):
    print('compiling pdf for ALL data...')
    pdf = PDF()
    pdf.add_page()
    print('---------------------------------')
    pdf.grapher('day_plot.png','dayplot')
    pdf.grapher('week_plot.png','week plot')
    for x in datafile:
        print('_______________I am just a debugging bug______________')
        pdf.maker('datologo.png', x)
    pdf.output('newManxx.pdf', 'F')
    print('pdf compiled successfully.')

