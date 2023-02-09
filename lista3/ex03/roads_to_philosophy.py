import requests
import sys
from bs4 import BeautifulSoup

def get_html(search):
    url = f"https://en.wikipedia.org{search}"
    # print(url)
    try:
        response = requests.get(url)
    except Exception as e: 
        return(f"Request error: {e}")
    if response.status_code == 200:
        return((True, response.text))
    else:
        return((False, f"Http error status code: {response.status_code}"))



def run(search):
    status, content = get_html(search)
    if status:
        soup = BeautifulSoup(content, 'html.parser')
        body_content = soup.find(id="bodyContent")
        links = body_content.select("p > a")
        if len(links) == 0:
            return("It's a dead end !")
        title = links[0].contents[0]
        next_link = links[0].get("href")
        if title in road:
            return("It leads to an infinite loop !")
        if title == "philosophy":
            road.append(title.title())
            return("philosophy")
        road.append(title.title())
        return(run(next_link))
    else:
        return(content)

def search_format(search):
    if "(" in search:
        temp = search.split(" ")
        return("_".join(temp))
    search = search.title()
    search = search.replace(" ","_")
    return(search)

if __name__ == '__main__':
    arg = sys.argv    
    if len(arg) == 2:
        road  = []
        search = search_format(arg[1])
        search = "/wiki/" + search
        status = run(search)
        if status != "philosophy":
            print(status)
        else:
            print(arg[1])
            for step in road:
                print(step)
            print(f"{len(road) -1} roads from {arg[1]} to philosophy !")
        
    else:
        print("Error: You need pass just ONE search parameter. E.g. python3 request_wikipedia.py \"Nelson Mandela\"")
