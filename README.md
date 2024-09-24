# Svit.ch Member Data Scraper

This Python script scrapes member data from the Svit.ch website and saves it to both JSON and CSV files.

## Requirements

* Python 3.x
* requests
* beautifulsoup4
* json
* csv

## Installation

1. Install the required packages:
```bash
pip install requests beautifulsoup4 json csv
```

## Usage

1. Run the script:
```bash
python main.py
```

## Output

The script will create two files:

* `parsed_data.json`: Contains the scraped data in JSON format.
* `parsed_data.csv`: Contains the scraped data in CSV format.

## Code Explanation

The script uses the `requests` library to make a POST request to the Svit.ch API endpoint. The response is then parsed using `BeautifulSoup` to extract the desired data. The extracted data is then saved to both JSON and CSV files.

## Notes

* The script uses a hardcoded `data` dictionary to specify the search parameters. You can modify this dictionary to change the search criteria.
* The script uses a hardcoded `cookies` dictionary to bypass the website's anti-scraping measures. You may need to update these cookies if they change.
* The script uses a hardcoded `headers` dictionary to mimic a real browser request. You may need to update these headers if they change.
* The script uses the `encode('ascii', 'ignore').decode('ascii')` method to remove any non-ASCII characters from the scraped data. This is necessary to avoid errors when saving the data to files.

## Disclaimer

This script is for educational purposes only. It is not intended for commercial use or to violate any website's terms of service.
```