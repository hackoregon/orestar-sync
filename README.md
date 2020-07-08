# OreStar-API

## Django API
Django Rest Framework 

## Seleinum Headless Web scrapper
Selenium automates browsers. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. We use it to interact with javascript generated components to naviagte through OreStar.

## OreStar
Orestar is a publically funded collection of Oregon State election financing data

## Build Image and Run API Image
```
./bin/build.sh -d
./bin/start.sh -d
```

## Run WebScraper
In order to scrape OreStar website
adjust the following lines to the appropriate date save and run the command below.
```
python manage.py transactionsByDate
```
This will generate a .csv file.
