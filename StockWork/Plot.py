##############################################
#Original Author: Tony Sanchez Sep 2018
#last edited by: Tony Sanchez
#last edit Date: 10-16-2018
#Description:
# This file will plot data 
#
#Dependancies: 
#    Python3.7
#    Matplotlib
#    
#
##Goals#
#  open file for reading
#  read data 
#  format data from string to float
#  invert the data to most recent on top(?) 
#  plot datas
##############################################

import csv 
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_stocks(stock):
     file = stock + "parsedStockData.txt"


     with open (file) as csvfile:
          readcsv =csv.reader(csvfile,delimiter=',')
          Dates=[]
          Prices=[]
          n=0
          
          #for loop starts here
          for row in readcsv:
               #gets the date from Row 7 and price from Row 5
               PriceStr = row[4]
               Price = float(PriceStr)
               DateStr = row[10]
		
               #appends Price and date to the lists
               Dates.append(datetime.strptime(DateStr,'%Y-%m-%d-%H:%M:%S'))
               Prices.append(Price)		     
               #print (Date)
               
               #for loop control:		     
               n=n+1
               #print (n)
               
               if n >390: # GUI controlled or = to maxloop in main.py
                    break

     #print (Dates)
     #print (Prices)
     
     plt.plot([],[])
     plt.scatter(Dates, Prices, s =50, c = 'red')
     # beautify the x-labels
     plt.gcf().autofmt_xdate()
     myFmt = mdates.DateFormatter('%Y-%m-%d-%H:%M:%S')
     plt.gca().xaxis.set_major_formatter(myFmt)
     

          
     
     plt.show()
     return(Prices)
     
