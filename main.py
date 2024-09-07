import requests
import time
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
from datetime import datetime
from request_config import cookies, headers

sys.dont_write_bytecode = True

def scrape_bids_with_requests(status: str = 'Open', rows_per_page: int = 10):
    """
    Scrape bid data from the Delaware government website using requests.

    This function sends POST requests to the Delaware government's bid website,
    retrieves bid data, handles pagination, and saves the results to a CSV file.

    Args:
        status (str, optional): The status of bids to retrieve. Defaults to 'Open'.
        rows_per_page (int, optional): Number of rows to retrieve per page. Defaults to 10.

    Returns:
        None. The function saves the scraped data to 'bids_requests.csv'.
    """
    
    params = {
        'status': status,
    }
    
    page = 1
    
    json_data = {
        '_search': False,
        'nd': int(time.time() * 1000),
        'rows': rows_per_page,
        'page': page,
        'sidx': 'OpenDate',
        'sord': 'desc',
    }
    
    ## handling pagination
    response = requests.post('https://mmp.delaware.gov/Bids/GetBids', params=params, cookies=cookies, headers=headers, json=json_data)
    total = response.json()['total']
    raw_data = []
    for page in range(1, total + 1):
        json_data['page'] = page
        response = requests.post('https://mmp.delaware.gov/Bids/GetBids', params=params, cookies=cookies, headers=headers, json=json_data)
        raw_data.extend(response.json()['rows'])
    df = pd.DataFrame(raw_data)
    df.to_csv('bids_requests.csv', index=False)
    
def scrape_bids_with_selenium():
    """
    Scrape bid data from the Delaware government website using Selenium.

    This function uses Selenium to navigate through the bid website,
    extract bid details, and save the results to a CSV file.

    Returns:
        None. The function saves the scraped data to 'bids_selenium.csv'.
    """
    
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    # detach the driver from the current process
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    # Open the webpage
    driver.get("https://mmp.delaware.gov/Bids/")    
    pages = driver.find_element(By.XPATH, '//*[@id="sp_1_jqg1"]')
    next_page_button = driver.find_element(By.XPATH, '//*[@id="next_jqg1"]/span')
    def extract_data(rows):
        datas = []
        for row in rows:
            id = row.get('id')
            if row.has_attr('tabindex') and row.has_attr('id'):
                row_data = row.find_all('td')[1:7]
                if len(row_data) == 6:  # Ensure we have all 6 columns
                    extracted_data = [td.text.strip() for td in row_data]
                    contract_number, title, open_date, deadline_date, agency_code, unspsc_code = extracted_data
                    # every td has its id, we need that id to get the details of the bid
                    data = {
                        'id': id,
                        'link': f'https://mmp.delaware.gov/Bids/Details/{id}',
                        'contract_number': contract_number,
                        'title': title,
                        'open_date': open_date,
                        'deadline_date': deadline_date,
                        'agency_code': agency_code,
                        'unspsc_code': unspsc_code
                    }
                    datas.append(data)
                else:
                    print(f"Skipping row: insufficient data ({len(row_data)} columns)")
            else:
                print("Skipping row: no tabindex attribute")
        return datas
    scraped_data = []    
    for page in range(1, int(pages.text) + 1):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        table_id = 'jqGridBids'
        table = soup.find('table', {'id': table_id})
        rows = table.find_all('tr')
        data = extract_data(rows)
        scraped_data.extend(data)
        try:
            next_page_button.click()
            time.sleep(5)
        except:
            print("No more pages to load")
            break
    df = pd.DataFrame(scraped_data)
    df.to_csv('bids_selenium.csv', index=False)

if __name__ == '__main__':
    """
    Main function to execute the scraping process based on command-line arguments.

    This function checks the command-line arguments and calls the appropriate scraping function.
    It supports two modes: 'requests' and 'selenium'.

    Usage:
        python main.py requests [status] [rows_per_page]
        python main.py selenium

    Args:
        None. The function uses command-line arguments to determine the mode and other parameters.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <mode> [status] [rows_per_page]")
        print("Modes: requests, selenium")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == 'requests':
        status = sys.argv[2] if len(sys.argv) > 2 else 'Open'
        rows_per_page = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        scrape_bids_with_requests(status, rows_per_page)
    elif mode == 'selenium':
        scrape_bids_with_selenium()
    else:
        print("Invalid mode. Use 'requests' or 'selenium'.")
        sys.exit(1)