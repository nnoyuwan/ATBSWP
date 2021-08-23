import requests
import bs4

print('请输入url:')
url = input()
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, features='html.parser')
a_list = soup.select('a')
print(a_list)
for a in a_list:
    a_url = a.get('href')
    response = requests.get(a_url)
    try:
        if response.status_code == requests.codes.not_found:
            print("Page %s is broken link" % a_url)
        else:
            print("Page %s is other type link" % a_url)
    except:
        print("Page %s is Error" % a_url)
