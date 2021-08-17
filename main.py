import requests
from bs4 import BeautifulSoup
from notification import sendBestBuyNotification

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

proxies = []
count = 0

with open('proxies.txt') as f:
    for line in f:
        line = line.strip()
        proxy = line.split(':')
        proxyHTTP = proxy[0] + ':' + proxy[1]
        proxies.append(proxyHTTP)
proxyCount = len(proxies)

while True:
    with open('bestBuySkus.txt') as f:
            for line in f:
                line = line
                sku = line.strip('\n')

                if proxyCount != 0:
                    requestProxy = {
                        "http": "http://" + proxies[count],
                        "https": "http://" + proxies[count],
                    }
                    count += 1
                else:
                    requestProxy = {}

                if count == proxyCount:
                    count = 0

                url = "https://www.bestbuy.com/site/" + sku + ".p?skuId=" + sku
                response = requests.request("GET", url, headers=headers)
                response.proxies = requestProxy

                soup = BeautifulSoup(response.text, 'html.parser')
                name = soup.find('h1', attrs={'class': 'heading-5 v-fw-regular'}).get_text()
                image = soup.find('img', attrs={'class': 'primary-image'})['src']
                price = soup.find('div', attrs={'class': 'priceView-hero-price'}).get_text().split('Your')[0]
                addToCart = 'https://api.bestbuy.com/click/-/' + sku + '/cart'
                availability = soup.find('button', attrs={'class': 'add-to-cart-button'}).get_text()

                if (availability != 'Sold Out'):
                    sendBestBuyNotification(sku, url, name, image, price, addToCart)
                else:
                    print(name + ' (' + sku + ') out of stock')