import requests
from bs4 import BeautifulSoup

url = "https://www.johnlewis.com/john-lewis-anyday-nova-office-chair-grey/p3585356"
res = requests.get(url)
status_code = res.status_code
content = res.content

if res.ok:
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find("span", {"data-testid": "product:price", "class": "Price_anydayPrice__30b5i"})

    string_value = element.text.strip()     # "£79.00"
    price = float(string_value[1:])         # conversion to float and removing currency symbol

    if price < 200:
        print("You should buy the chair!")
    elif price == 200:
        print("Buy at your own peril!")
    else:
        print("It's expensive, don't buy.")
else:
    print("HTTP Status Code: ", status_code)


# <span data-testid="product:price" class="Price_anydayPrice__30b5i">£79.00</span>