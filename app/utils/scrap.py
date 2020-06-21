# This file handles Scraping of the data, storing it to the database and creating a csv file also for the same
import pathlib
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
        parsed_data = []
        # get table body only
        table_body_data = soup.find('tbody')
        for row in table_body_data.find_all('tr'):
            table_data = row.find_all('td')
            table_row_data = {
                "date": table_data[0].text, "price": table_data[1].text,
                "open_price": table_data[2].text, "highest_price": table_data[3].text,
                "lowest_price": table_data[4].text, "volume": table_data[5].text,
                "percentage_change": table_data[6].text,
            }
            parsed_data.append(table_row_data)
        return parsed_data

    def store_in_csv(self, data, file_name):
        ''' Store scrapped data to a csv file'''

        csv_folder = pathlib.Path.cwd() / 'app' / 'resource'

        with open(f'{csv_folder}/{file_name}.csv', 'w') as csv_file:
            fieldnames = ['date', 'price', 'open_price', 'highest_price',
                          'lowest_price', 'volume', 'percentage_change']
            csv_writer = csv.DictWriter(
                csv_file,  fieldnames=fieldnames, delimiter=',')

            csv_writer.writeheader()

            for single_day_data in data:
                csv_writer.writerow(single_day_data)

    def store_in_db(self, data):
        ''' store the scrapped data to the database '''
        (date, price, open_price, highest_price,
         lowest_price, volume, percentage_change) = data
