import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)



def create_custom_hn(links, subtext):
    hn = []
    for indx, item in enumerate(links):
        title = item.getText()
        href = item.find(href=True)
        vote = subtext[indx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


# Driver Code
if __name__ == '__main__':
    pprint.pprint(create_custom_hn(links, subtext))
