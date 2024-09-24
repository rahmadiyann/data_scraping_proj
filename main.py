import requests
from bs4 import BeautifulSoup
import json
import csv

cookies = {
    'googtrans': '/de/en',
    'googtrans': '/de/en',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'googtrans=/de/en; googtrans=/de/en',
    'dnt': '1',
    'origin': 'https://www.svit.ch',
    'priority': 'u=1, i',
    'referer': 'https://www.svit.ch/de/members?title=&city_name=&field_member_city_target_id=All&field_cities_coordinates_proximity=0&organisation_id=&field_membership_type_target_id%5B65%5D=65&sort_by=field_company_value&page=1',
    'sec-ch-ua': '"Chromium";v="129", "Not=A?Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'mo_id': '',
    'city_id': 'All',
    'proximity': '0',
    'membership_type': '65',
    'name': '',
    'locality': '',
    'activities': '',
}

response = requests.post('https://www.svit.ch/de/svit/members/json', cookies=cookies, headers=headers, data=data)

parsed_data = []
datas = response.json()
id = 1
for data in datas:
    html_content = data['content']
    soup = BeautifulSoup(html_content, 'html.parser')
    member_title = soup.find('div', class_='member-title').text.strip() if soup.find('div', class_='member-title') else "None"
    member_name = soup.find('div', class_='member-name').text.strip() if soup.find('div', class_='member-name') else "None"
    membership_type = soup.find('div', class_='membership-type').text.strip() if soup.find('div', class_='membership-type') else "None"
    member_svit_mo = soup.find('div', class_='member-svit-mo').text.strip() if soup.find('div', class_='member-svit-mo') else "None"
    member_street = soup.find('div', class_='member-street').text.strip() if soup.find('div', class_='member-street') else "None"
    member_zip_city = soup.find('div', class_='member-zip-city').text.strip() if soup.find('div', class_='member-zip-city') else "None"  
    member_email = soup.find('div', class_='member-email').text.strip() if soup.find('div', class_='member-email') else "None"
    member_website = soup.find('div', class_='member-website').text.strip() if soup.find('div', class_='member-website') else "None"
    
    data = {
        'id': id,
        'member_title': member_title.encode('ascii', 'ignore').decode('ascii') if member_title else "None",
        'member_name': member_name.encode('ascii', 'ignore').decode('ascii') if member_name else "None",
        'membership_type': membership_type.encode('ascii', 'ignore').decode('ascii') if membership_type else "None",
        'member_svit_mo': member_svit_mo.encode('ascii', 'ignore').decode('ascii') if member_svit_mo else "None",
        'member_street': member_street.encode('ascii', 'ignore').decode('ascii') if member_street else "None",
        'member_zip_city': member_zip_city.encode('ascii', 'ignore').decode('ascii') if member_zip_city else "None",
        'member_email': member_email.encode('ascii', 'ignore').decode('ascii') if member_email else "None",
        'member_website': member_website.encode('ascii', 'ignore').decode('ascii') if member_website else "None"
    }
    
    parsed_data.append(data)
    id += 1
    
with open('parsed_data.json', 'w') as f:
    json.dump(parsed_data, f, indent=4)
    
with open('parsed_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=parsed_data[0].keys())
    writer.writeheader()
    writer.writerows(parsed_data)