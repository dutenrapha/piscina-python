import sys

def title_list(word_list):
    temp = [word.strip().title() for word in word_list]
    return temp


def run(arg):
    sentence = arg[1]
    sentence = sentence.split(",")
    sentence = title_list(sentence)

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
    for candidate in sentence:
        if candidate:
            # print(f"{candidate} - {states.keys()} - {capital_cities.values()}")
            # if candidate in capital_cities.values() or candidate in states.keys():
            if candidate in capital_cities.values():
                print(f"{candidate} is the capital of {inv_states[inv_capital_cities[candidate]]}")
            elif candidate in states.keys():
                print(f"{candidate} is a state")
            else:
                print(f"{candidate} is neither a capital city nor a state")

if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 2: 
        run(arg)