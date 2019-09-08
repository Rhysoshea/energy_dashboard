# UK Energy Dashboard
A repository to showcase the code used to create a locally hosted dashboard for the UK energy spot market
[More information](https://medium.com/@rhysshea/my-first-solo-programming-project-db1f6c183c39)

## Purpose
A simple project to build from the ground up and put to practice my recently acquired knowledge of Python and JavaScript into a practical example.

I also wanted to work on something that I have a personal interest in and that I could showcase using data.


## Data
This dashboard updates every 30 minutes and requests up-to-date data from Elexon, the UK regulator for energy.
The data pulled through the API includes:
- latest energy demand of the UK in MW
- latest energy generation of the UK in MW, as well as a breakdown of energy sources
- interconnector flows from neighbouring countries
- a forecast of generation available over the next 12 months
- a forecast of demand expected over the next 12 months
- the latest system frequency (a balance of of supply and demand)
- the latest market prices of energy in £/MWh and the volume traded every 30 minutes

Other data:
- weather forecast of temperature, rainfall and wind speed
- news headlines


## Technologies used
1. Python
  - http-server [path] [options] for locally hosting the dashboard
  - pandas and numpy for data cleaning
  - httplib for interacting with several site APIs and collecting data
  - BeautifulSoup for data parsing
2. JavaScript
  - JS was used to serve up the cleaned data to a webpage that could be modified using HTML and CSS
  - highcharts a graphical JS library that creates interactive graphs

![](images/architecture.png)
