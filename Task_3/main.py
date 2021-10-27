import requests
from datetime import datetime
from pprint import pprint


def get_questions(tag):
    end_date = int(datetime.timestamp(datetime.now()))
    start_date = end_date - 2 * 86400

    params = {
        'fromdate': start_date,
        'todate': end_date,
        'tagged': tag,
        'site': 'stackoverflow'
    }

    resp = requests.get('https://api.stackexchange.com/2.3/questions', params=params)
    pprint(resp.json())
    if resp.status_code == 200:
        print("GOOD")
    else:
        exit(resp.raise_for_status())
    total = 0
    for question in resp.json().get('items'):
        total += 1
        print('_________________________________________')
        print(f"Question: {question['title']}".upper())
        print(f"Tags: {str(question['tags'])}")
        print(f"Creation_date: {datetime.utcfromtimestamp(question['creation_date']).strftime('%Y-%m-%d %H:%M:%S')}")
        print('_________________________________________')
        print()
    print(f"TOTAL: {total}")


get_questions('python')
