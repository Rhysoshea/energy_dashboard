
import csv
from bs4 import BeautifulSoup
import httplib2
import numpy as np
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta

API = 'mlplmmd3biqahbq'

def main ():
    start_date = (dt.now()-timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    end_date = (dt.now()).strftime("%Y-%m-%d %H:%M:%S")
    http_obj = httplib2.Http()
    resp, content = http_obj.request(
        uri='https://api.bmreports.com/BMRS/FREQ/v1?APIKey=' + API + '&FromDateTime='+start_date+'&ToDateTime='+end_date+'&ServiceType=csv',
        method='GET',
        headers={'Content-Type':'application/csv: charset=UTF-8'}
    )

    with open('./data/frequency.csv', 'w') as file:
        writer = csv.writer(file)
        reader = csv.reader(content.splitlines())

        for row in reader:
            writer.writerow(row)


if __name__ == "__main__":
    main()
