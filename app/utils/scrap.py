# This file handles Scraping of the data, storing it to the database and creating a csv file also for the same
import requests
import csv
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
url = "https://www.investing.com/instruments/HistoricalDataAjax"


class ScrapParsePersist:

    def scrap(self, payload, headers):
        ''' Scraps data from investing.com '''
        try:
            response = requests.post(url, data=payload, headers=headers)

            # raise HTTPError if request returned an unsuccessful status code.
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error: {http_err}')
        except Exception as err:
            print(f'Error occurred: {err}')
        else:
            return response.text

    def parse_data(self, source):
        ''' pull data out of HTML '''
        soup = BeautifulSoup(source, 'lxml')
        # Todo
        print(soup)

    def store_in_csv(self, data, file_name):
        ''' Store scrapped data to a csv file'''

        with open(f'../resource/{file_name}', 'w') as csv_file:
            fieldnames = ['Date', 'Price', 'Open Price', 'Highest Price',
                          'Lowest Price', 'Volume', 'Percentage Change']
            csv_writer = csv.DictWriter(
                csv_file,  fieldnames=fieldnames, delimiter=',')

            csv_writer.writeheader()

            for single_day_data in data:
                csv_writer.writerow(
                    [single_day_data['date'], single_day_data['price'],
                     single_day_data['open_price'],
                     single_day_data['highest_price'],
                     single_day_data['lowest_price'],
                     single_day_data['volume'],
                     single_day_data['percentage_changes'], ])

    def store_in_db(self, data):
        ''' store the scrapped data to the database '''
        (date, price, open_price, highest_price,
         lowest_price, volume, percentage_change) = data
