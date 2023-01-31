import sys

def run(arg):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    print(arg)

if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 2: 
        run(arg)