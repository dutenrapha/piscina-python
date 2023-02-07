import requests
import json
import sys
from dewiki import from_string

def run():
    url = "https://en.wikipedia.org/w/api.php"
    search = "chocolate"
    response = requests.get(url, params={"action":"query", "list":"search", "srsearch":search, "format":"json"})
    response = response.json()
    title = response["query"]["search"][0]["title"]

    response = requests.get(url, params={"action":"parse", "page":title, "format":"json"})
    data = response.json()
    # print(data["parse"].keys())
    # print(data["parse"]["text"]["*"])
    a = from_string(data["parse"]["text"]["*"])
    # print(a)
    print(data["parse"].keys())
    print(data["parse"]["revid"])
if __name__ == '__main__':
    run()

