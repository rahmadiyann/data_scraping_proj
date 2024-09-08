# Cookies and headers are obtained from the browser's network tab under the request that is made
# To obtain cookies and headers, you can use the following steps:
# 1. Open the browser's network tab and filter the requests.
# 2. Find the request that is made to the Delaware government website.
# 3. Right click on the request and click on "Copy as cURL"
# 4. Paste the cURL command into a tool like Postman to get the cookies and headers

cookies = {
    '.AspNetCore.Mvc.CookieTempDataProvider': 'CfDJ8IUHoBbyZ9hDuxl3hqS4t_o7Nlolx3BR_5L4kTbeNmZZ_BJ5nX8OMlLQwksazvCT0Ijv5SMMxUyDm0G3KY5jpX14SO_6JV9fcyNqdJ3FcV1K6u5zEkL1kF2N5x-8Z3b3kMIKkzLFB5QK71BYNdEjr3E',
    'TS01514f0c': '01761ac5de7f27af76358baaef4700066d5f6ea88ec7557cd044b100e27c44160e5d758d9d3b8e962cb8029116a6107f7ab4c662ef07c2b7a4391e58691235ed41daca3bfb',
    'TS763bccd8027': '086434786fab20002b89c374514a95441a6ad2d4262d904931188ce5c0283b0b8786e969d47cb6540867178a761130008e4aa4c90b968a7680bb260d8b8d66eac48a0779a539d9132d43f1c6170a67176736a4aea5cd18cc57d3ac8d8fba3c4b',
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'DNT': '1',
    'Origin': 'https://mmp.delaware.gov',
    'Referer': 'https://mmp.delaware.gov/Bids/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}