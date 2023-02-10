import requests
import sys
from dewiki import from_string

def gen_wiki_file(wikitext, search):
    file_name = search.replace(" ", "_")
    file_wiki = open(f"{file_name}.wiki", "w")
    file_wiki.write(wikitext)
    file_wiki.close()

def run(search):
    url = "https://en.wikipedia.org/w/api.php"
    try:
        response = requests.get(url, params={"action":"parse", "page":search, "prop":"wikitext", "format":"json", "redirects":"True"})
    except Exception as e: 
        return(f"Request error: {e}")
    if response.status_code == 200:
        response = response.json()
        if "error" in response.keys():
            return(response["error"]["info"])
        else:
            wikitext = response["parse"]["wikitext"]["*"]
            gen_wiki_file(wikitext, search)
            text = from_string(wikitext)
            return(text)
    else:
        return(f"Http error status code: {response.status_code}")
if __name__ == '__main__':
    arg = sys.argv    
    if len(arg) == 2:
        print(run(arg[1]))
    else:
        print("Error: You need pass just ONE search parameter. E.g. python3 request_wikipedia.py \"Nelson Mandela\"")


