# Cross Country Mortgage Loan Officer Scraper

This Python script scrapes loan officer information from Cross Country Mortgage's website.

## Usage

1. **Install dependencies:**
   ```bash
   pip install requests
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

   This will create a `data.json` file containing the scraped loan officer data.

## Configuration

The script uses hardcoded values for IP address, latitude, longitude, and zip code. You can modify these values in the `if __name__ == '__main__':` block to target a specific location.

## Data Structure

The `data.json` file contains a list of dictionaries, each representing a loan officer. Each dictionary has the following keys:

- `employee_id`
- `first_name`
- `last_name`
- `username`
- `email`
- `phone_number`
- `marketing_job_title`
- `branch_number`
- `url`
- `streetaddressline1`
- `streetaddressline2`
- `city`
- `county`
- `state`
- `zipcode`
- `country`
- `latitude`
- `longitude`

## Disclaimer

This script is for educational purposes only. It is not intended for any illegal or unethical activities. Please respect the website's terms of service and use this script responsibly.