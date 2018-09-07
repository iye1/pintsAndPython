#Author: Idris El
#Last edited by: Idris El
#Last edited date: 9/5/2018
#
#python 3.7
#
#To run this program you will NEED access to the requests library
#See link below for more information
#http://docs.python-requests.org/en/master/
#You will also need a key from the AlphaVantage website if the key no longer works
#also refer to AlphaVantage documentation for API call structure
#https://www.alphavantage.co/documentation/

#
#This function makes an API call to AlphaAdvantage and retrieves
#the most up to date info on a specific stock or cryptocurrency.
#The data is then stored in a CSV file for further modification

import requests

def get_stock_CSV():
    #API key from alphaVantage
    aKey = 'N4CIZVQRUR484FTE'
    file = "ETHstockData.txt"


    #Passing parameters to construct proper URL
    #This specific call retrieves the most recent quote for a stock
    payload = {'function': 'GLOBAL_QUOTE', 'symbol':'ETH', 'apikey':'aKey', 'datatype':'csv'}
    r = requests.get('https://www.alphavantage.co/query',params=payload)

    #If successful, save data to file that either exists or will be created
    if r.status_code == 200:
        out = open(file,"w")
        out.write(r.text)
        out.close()
        print(f"Created File: {file}\n")

    #If not successful, print error code
    else:
        print (r.status_code)





#FUNCTION OPTIONS *NOTE: you WILL have to see how to structute param from
#the api documentation as they differ.
    
#Intraday: 'TIME_SERIES_INTRADAY'
#Daily: 'TIME_SERIES_DAILY'
#Weekly: 'TIME_SERIES_WEEKLY'
#Monthly: 'TIME_SERIES_MONTHLY'


