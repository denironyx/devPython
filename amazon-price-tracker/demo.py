from requests_html import HTMLSession

s = HTMLSession()

r = s.get('https://www.amazon.com/dp/B0759GN2WL/')

r.html.render(sleep=1)

price = r.html.find('#priceblock_ourprice')[0].text
title = r.html.find('#productTitle')[0].text

print(title)
print(price)
