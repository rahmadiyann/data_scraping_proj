# Delaware Government Bid Scraper

This Python script scrapes bid data from the Delaware government website using two different methods: requests and Selenium.

## Features

- Scrapes bid data using either requests or Selenium
- Handles pagination
- Saves results to CSV files

## Usage

1. Install dependencies:
   ```
   pip install requests beautifulsoup4 selenium pandas
   ```

2. Run the script:
   ```
   python main.py <mode> [status] [rows_per_page]
   ```
   
   Modes:
   - `requests`: Uses the requests library
   - `selenium`: Uses Selenium WebDriver

   Optional arguments:
   - `status`: Bid status (default: 'Open')
   - `rows_per_page`: Number of rows per page (default: 10)

## Output

- `bids_requests.csv`: Output file for requests mode
- `bids_selenium.csv`: Output file for Selenium mode

## Note

Ensure you have the necessary credentials in `request_config.py` for the requests mode.