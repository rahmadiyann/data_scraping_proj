import requests
import json

def fetch_info(ip_address: str, longitude: float, latitude: float, zipcode: int) -> dict:
    cookies = {
        'CMSPreferredCulture': 'en-US',
        'ASP.NET_SessionId': 'xexttd1sryzdnp3gv3zayhki',
        '__cf_bm': 'BkxkaeRtC_SzxjWIIvIPZbesrJvq1itgb_yh5oywqFs-1727216311-1.0.1.1-NFWVMTYr4ksI679YmINPbL0xLChopH7ZJ.vKkF9euUC1__DOkeWutiDwA4uTnr4DS18lRmLWAv32pQ7YbyTxZw',
        'cf_clearance': 'ct.oLACaXMJV9KRBm7M5ntVTcyasvUKLTqnVz0UumLQ-1727216313-1.2.1.1-uVv2yb6TaH31QdhERBA4.TfTieptqcd3b50pm6v3dKLGCBKrPmundz2Qls1LT7im3vq4mLvJ4BhHnbXw.I04XpXzfaIQhA39cG2Tan3X04qLN824Kr4IW0MBITo_HLRGD4qhb4pwkrCDGBkfOkPrKbFsR.dX5.8wkCI3maW4kYfZOlqqvs997_cH2tmn9IXHG5rMWwUXh6sHr2XtmnZpHnbc0dE2XwdmbdpWzxXVoQ..Ik2GRavJLErM7o8fLFOKTvlngi9rGcH3IUR89M4U1ODHQuMai0W_OglsTQ8R6bqPbNi1TZEzhG.o7Du.0sTihVsG53rwIdJPB0ScvhCms3nYs0i2.ianDzN5JvqFunMlY1PUy0MYr.SYR1WZnAgDuFgCb6GNxhXRu75C1jwSSg',
        'CCM_LOFollowID': '58646',
        'CCM_LOFollowMeta': '%7b%22NodeAlias%22%3a%22384364-Renzo-Odria%22%2c%22Name%22%3a%22Renzo%20Odria%22%2c%22NMLS%22%3a%22384364%22%2c%22ApplyNowURL%22%3a%22https%3a%2f%2fapp.crosscountrymortgage.com%2f%23%2fsignup%3freferrerId%3drenzo.odria%2540ccm.com%22%2c%22QuickQuoteURL%22%3a%22https%3a%2f%2fforms.crosscountrymortgage.com%2floan%2ffree-rate-quote%3flonmlsid%3d384364%26branchid%3d3859%22%2c%22RelativeURL%22%3a%22%7e%2fNewark-DE-3859%2fRenzo-Odria%2f%22%2c%22HelocURL%22%3a%22%22%2c%22HasBlogPosts%22%3a%22False%22%7d',
        'CCM_ChicagoRRIsActive': 'false',
        'CCM_EpsilonStartIsActive': 'false',
        'AWSALBTG': 'VL3mdil+bQfHNNVzkrTf0bKR9KLtyvUKKgjIzaLBdp0Qbu4YA5DuB9Bky3+4ZbG1UczYsSndfAEWl12vN14zHgUziaxHwld0pMm5hrAwapT8TEAL+++XjH6OX8g8bmHUs1gIZptCFg8a8pVQf9dG7dP11QxFlOwkwARvN07d6LWSxbdD+38=',
        'AWSALBTGCORS': 'VL3mdil+bQfHNNVzkrTf0bKR9KLtyvUKKgjIzaLBdp0Qbu4YA5DuB9Bky3+4ZbG1UczYsSndfAEWl12vN14zHgUziaxHwld0pMm5hrAwapT8TEAL+++XjH6OX8g8bmHUs1gIZptCFg8a8pVQf9dG7dP11QxFlOwkwARvN07d6LWSxbdD+38=',
        'AWSALB': '3cRA01UcPG4qXvBifTrBr6XIxugntyJ7eAKEqq97qlJFxt1d5UpBkpJDz7gn7wZ/OOuwnU9VoH6FmTgU485pIWeKZyAw6hWF7af8XDpB54gtF+maB+16L5ibnudH',
        'AWSALBCORS': '3cRA01UcPG4qXvBifTrBr6XIxugntyJ7eAKEqq97qlJFxt1d5UpBkpJDz7gn7wZ/OOuwnU9VoH6FmTgU485pIWeKZyAw6hWF7af8XDpB54gtF+maB+16L5ibnudH',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': 'CMSPreferredCulture=en-US; ASP.NET_SessionId=xexttd1sryzdnp3gv3zayhki; __cf_bm=BkxkaeRtC_SzxjWIIvIPZbesrJvq1itgb_yh5oywqFs-1727216311-1.0.1.1-NFWVMTYr4ksI679YmINPbL0xLChopH7ZJ.vKkF9euUC1__DOkeWutiDwA4uTnr4DS18lRmLWAv32pQ7YbyTxZw; cf_clearance=ct.oLACaXMJV9KRBm7M5ntVTcyasvUKLTqnVz0UumLQ-1727216313-1.2.1.1-uVv2yb6TaH31QdhERBA4.TfTieptqcd3b50pm6v3dKLGCBKrPmundz2Qls1LT7im3vq4mLvJ4BhHnbXw.I04XpXzfaIQhA39cG2Tan3X04qLN824Kr4IW0MBITo_HLRGD4qhb4pwkrCDGBkfOkPrKbFsR.dX5.8wkCI3maW4kYfZOlqqvs997_cH2tmn9IXHG5rMWwUXh6sHr2XtmnZpHnbc0dE2XwdmbdpWzxXVoQ..Ik2GRavJLErM7o8fLFOKTvlngi9rGcH3IUR89M4U1ODHQuMai0W_OglsTQ8R6bqPbNi1TZEzhG.o7Du.0sTihVsG53rwIdJPB0ScvhCms3nYs0i2.ianDzN5JvqFunMlY1PUy0MYr.SYR1WZnAgDuFgCb6GNxhXRu75C1jwSSg; CCM_LOFollowID=58646; CCM_LOFollowMeta=%7b%22NodeAlias%22%3a%22384364-Renzo-Odria%22%2c%22Name%22%3a%22Renzo%20Odria%22%2c%22NMLS%22%3a%22384364%22%2c%22ApplyNowURL%22%3a%22https%3a%2f%2fapp.crosscountrymortgage.com%2f%23%2fsignup%3freferrerId%3drenzo.odria%2540ccm.com%22%2c%22QuickQuoteURL%22%3a%22https%3a%2f%2fforms.crosscountrymortgage.com%2floan%2ffree-rate-quote%3flonmlsid%3d384364%26branchid%3d3859%22%2c%22RelativeURL%22%3a%22%7e%2fNewark-DE-3859%2fRenzo-Odria%2f%22%2c%22HelocURL%22%3a%22%22%2c%22HasBlogPosts%22%3a%22False%22%7d; CCM_ChicagoRRIsActive=false; CCM_EpsilonStartIsActive=false; AWSALBTG=VL3mdil+bQfHNNVzkrTf0bKR9KLtyvUKKgjIzaLBdp0Qbu4YA5DuB9Bky3+4ZbG1UczYsSndfAEWl12vN14zHgUziaxHwld0pMm5hrAwapT8TEAL+++XjH6OX8g8bmHUs1gIZptCFg8a8pVQf9dG7dP11QxFlOwkwARvN07d6LWSxbdD+38=; AWSALBTGCORS=VL3mdil+bQfHNNVzkrTf0bKR9KLtyvUKKgjIzaLBdp0Qbu4YA5DuB9Bky3+4ZbG1UczYsSndfAEWl12vN14zHgUziaxHwld0pMm5hrAwapT8TEAL+++XjH6OX8g8bmHUs1gIZptCFg8a8pVQf9dG7dP11QxFlOwkwARvN07d6LWSxbdD+38=; AWSALB=3cRA01UcPG4qXvBifTrBr6XIxugntyJ7eAKEqq97qlJFxt1d5UpBkpJDz7gn7wZ/OOuwnU9VoH6FmTgU485pIWeKZyAw6hWF7af8XDpB54gtF+maB+16L5ibnudH; AWSALBCORS=3cRA01UcPG4qXvBifTrBr6XIxugntyJ7eAKEqq97qlJFxt1d5UpBkpJDz7gn7wZ/OOuwnU9VoH6FmTgU485pIWeKZyAw6hWF7af8XDpB54gtF+maB+16L5ibnudH',
        'dnt': '1',
        'origin': 'https://crosscountrymortgage.com',
        'priority': 'u=1, i',
        'referer': 'https://crosscountrymortgage.com/find-a-loan-officer/',
        'sec-ch-ua': '"Chromium";v="129", "Not=A?Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'option': 'location',
        'value': str(zipcode),
        'ip': ip_address,
        'lat': latitude,
        'lon': longitude,
    }
    
    response = requests.post('https://crosscountrymortgage.com/api/MasterDataInfo', cookies=cookies, headers=headers, json=json_data)
    return response.json()

def parse(response: dict) -> dict:
    
    if response['LoanOfficers'] == []:
        return None
    
    parsed_data = []
    for data in response['LoanOfficers']:
        employee_id = data['EmployeeId'] if 'EmployeeId' in data else None
        first_name = data['FirstName'] if 'FirstName' in data else None 
        last_name = data['LastName'] if 'LastName' in data else None
        username = data['Username'] if 'Username' in data else None
        email = data['EmailAddress'] if 'EmailAddress' in data else None
        phone_number = data['PhoneNumber'] if 'PhoneNumber' in data else None
        marketing_job_title = data['MarketingJobTitle'] if 'MarketingJobTitle' in data else None
        branch_number = data['BranchNumber'] if 'BranchNumber' in data else None
        url = data['LOBranchUrl'] if 'LOBranchUrl' in data else None
        streetaddressline1 = data['Address']['StreetAddressLine1'] if 'StreetAddressLine1' in data['Address'] else None
        streetaddressline2 = data['Address']['StreetAddressLine2'] if 'StreetAddressLine2' in data['Address'] else None
        city = data['Address']['City'] if 'City' in data['Address'] else None
        county = data['Address']['County'] if 'County' in data['Address'] else None
        state = data['Address']['State'] if 'State' in data['Address'] else None
        zipcode = data['Address']['ZipCode'] if 'ZipCode' in data['Address'] else None
        country = data['Address']['Country'] if 'Country' in data['Address'] else None
        latitude = data['Address']['Latitude'] if 'Latitude' in data['Address'] else None
        longitude = data['Address']['Longitude'] if 'Longitude' in data['Address'] else None
        parsed_data.append({
            'employee_id': employee_id,
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'phone_number': phone_number,
            'marketing_job_title': marketing_job_title,
            'branch_number': branch_number,
            'url': url,
            'streetaddressline1': streetaddressline1,
            'streetaddressline2': streetaddressline2,
            'city': city,
            'county': county,
            'state': state,
            'zipcode': zipcode,
            'country': country,
            'latitude': latitude,
            'longitude': longitude,
        })
        
    return parsed_data

def main(ip_address: str, longitude: float, latitude: float, zipcode: int) -> dict:
    response = fetch_info(ip_address, longitude, latitude, zipcode)
    return parse(response)

if __name__ == '__main__':
    
    # random ip
    ip = '159.92.4.171'
    # random lat and lon
    lat = 25.34886
    lon = -89.04727
    # random us zipcode
    zipcode = 48160
    
    with open('data.json', 'w') as f:
        json.dump(main(ip, lon, lat, zipcode), f, indent=4)