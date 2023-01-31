import sys

def run(arg):
    capital = arg[1]
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    inv_states = {v: k for k, v in states.items()}
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    inv_capital_cities = {v: k for k, v in capital_cities.items()}

    if capital not in capital_cities.values():
        print("Unknown state")
    else:
        print(inv_states[inv_capital_cities[capital]])

if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 2: 
        run(arg)