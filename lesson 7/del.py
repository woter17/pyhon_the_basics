import requests
from fake_useragent import UserAgent
import json

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://app.uniswap.org',
    'priority': 'u=1, i',
    'referer': 'https://app.uniswap.org/',
    'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': UserAgent().random,
    'x-api-key': 'JoyCGj29tT4pymvhaGciK4r1aIPvqW6W53xT1fwo',
    'x-app-version': '',
    'x-request-source': 'uniswap-web',
    'x-universal-router-version': '1.2',
}

json_data = {
    'type': 'EXACT_INPUT',
    'amount': '1000000000000000',
    'swapper': '0x23086FDE12270070c16124aC950B6bE2b4857E13',
    'tokenInChainId': 8453,
    'tokenOutChainId': 8453,
    'tokenIn': '0x0000000000000000000000000000000000000000',
    'tokenOut': '0x4ed4e862860bed51a9570b96d89af5e1b0efefed',
    'gasStrategies': [
        {
            'limitInflationFactor': 1.5,
            'priceInflationFactor': 1.5,
            'percentileThresholdFor1559Fee': 75,
            'minPriorityFeeGwei': 2,
            'maxPriorityFeeGwei': 99,
        },
    ],
    'urgency': 'normal',
    'protocols': [
        'V3',
        'V2',
    ],
}

response = requests.post('https://trading-api-labs.interface.gateway.uniswap.org/v1/quote', headers=headers, json=json.dumps(json_data))
print(response.status_code)
