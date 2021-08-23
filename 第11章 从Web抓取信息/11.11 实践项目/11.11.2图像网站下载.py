import os

import requests
import bs4, re

url = 'https://imgur.com/hot/time'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, features='html.parser')

img_dir = 'imgur'
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
result_set = soup.select('.image-list-link img')

p = re.compile(r'[^/]+(?!.*/)')
for img in result_set:
    img_url = 'http:' + img.get('src')
    basename = p.search(img_url).group()
    img_file = open(os.path.join(img_dir, basename), 'wb')
    img_res = requests.get(img_url)
    for chunk in img_res.iter_content(100000):
        img_file.write(chunk)
    img_file.close()
