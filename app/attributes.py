import requests
from bs4 import BeautifulSoup

def get_ancient_history():
    l = []
    d = {}

    url = "https://en.wikipedia.org/wiki/Timeline_of_ancient_history"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')

    for ul in soup.find_all("ul"):
        for li in soup.find_all("li"):
            if ': ' in li.text and "<a" in li.text:

                num1 = (li.text).split(": ")[0]
                num2 = (num1).split("-")[0]
                num3 = (num2).split(" to ")[0]
                num4 = (num3).split(" or ")[0]
                num5 = (num4).split("/")[0]

                print(num5)

                year = ''.join(x for x in num5 if x.isdigit())

                if 'BC' in num1:
                    year = int(year) * -1

                # Save year to dictionary
                d["year"] = int(year)
                # Save description to dictionary
                d["description"] = (li.text).split(": ")[1]
                # Appends dictionary to list
                l.append(d)
                d={}
    print(l)
    return l
