import sys

def run(arg):
    state = arg[1]
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
    if state not in states.keys():
        print("Unknown state")
    else:
        print(capital_cities[states[state]])

if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 2: 
        run(arg)