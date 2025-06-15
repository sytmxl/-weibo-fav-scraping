import os
import requests
import json
import time

def fetch_weibo_favorites(uid, page):
    url = "https://weibo.com/ajax/favorites/all_fav"
    params = {
        'uid': uid,
        'page': page,
        'with_total': True
    }
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Cookie': 'XSRF-TOKEN=BCorFfSMg-Bx-CZYiF3Zl8J0; _s_tentry=www.google.com.hk; Apache=9334402587852.344.1718184826723; SINAGLOBAL=9334402587852.344.1718184826723; ULV=1718184826725:1:1:1:9334402587852.344.1718184826723:; UOR=www.google.com.hk,open.weibo.com,www.google.com.hk; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFgH4XJPLNUQmcD6CjlGSMi5JpX5KMhUgL.Foe4eK-peKMReh.2dJLoI7L0IgDEIs90MNet; ALF=1725732305; SUB=_2A25LsXiBDeRhGeVH6lcQ8SnEyzWIHXVoz_RJrDV8PUJbkNB-LU_SkW1NT3tK951HQrl9o2Ex82VjQPY1VNKktpZR; WBPSESS=rIX0xaVszzoYPzPltHAy5rvWhGXFK0AmKF9R9O-I5hE3h4l8089O6Q1UQi6jKGHnAXme61UVLALxEaRLHJWOsKIDaboWTHzua1LxR1r8ywLxGZ3xSsm9W9vhcCaMziuWCJsLXK6n0lzNs82eCkJbOw=='
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def save_to_json(data, folder, page):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, f'favorites_page_{page}.json')
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def fetch_all_favorites(uid, folder='favorites'):
    # Fetch total number of favorites
    initial_data = fetch_weibo_favorites(uid, 1)
    if initial_data:
        total = initial_data.get('data').get('total_number')
        print(f"Total favorites: {total}")

        pages = (total // 20) + 1
        for page in range(1, pages + 1):
            print(page)
            data = fetch_weibo_favorites(uid, page)
            if data:
                save_to_json(data, folder, page)
            else:
                break
            time.sleep(1)  # Wait for 1 second between requests

        print(f"All favorites have been saved in the '{folder}' folder.")
    else:
        print("Failed to retrieve initial data.")

# Example usage
fetch_all_favorites('3915117809')
