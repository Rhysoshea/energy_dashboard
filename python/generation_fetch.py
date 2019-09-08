
import csv
from bs4 import BeautifulSoup
import httplib2
import numpy as np
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta

API = 'mlplmmd3biqahbq'

def main ():
    http_obj = httplib2.Http()
    resp, content = http_obj.request(
        uri='https://api.bmreports.com/BMRS/FOU2T52W/v1?APIKey='+ API +'&ServiceType=csv',
        method='GET',
        headers={'Content-Type':'application/csv: charset=UTF-8'}
    )
    # print (content)
    with open('./data/forecast_gen.csv', 'w') as file:
        writer = csv.writer(file)
        reader = csv.reader(content.splitlines())
        reader.next()
        writer.writerow(['ignore','Fuel', 'Date', 'Zone', 'Week', 'Year', 'MW'])
        for row in reader:
            writer.writerow(row)


if __name__ == "__main__":
    main()
