import requests
from bs4 import BeautifulSoup as BS
import re
a = []
urls = []
URL = "https://freelance.habr.com/tasks?q=парсер"
def pars():
    r = requests.get(URL)
    soup = BS(r.text , 'html.parser')
    for link in soup.find_all('a'):
        a.append(link.get('href'))

        #print (a)
    for i in a:
        m = re.search(".+tasks\/.+", i)
        if m!= None: 
            n = m.group()
            urls.append("https://freelance.habr.com" + n)
    return(urls)


if __name__ == '__main__':
    pars()