import sys
from antigravity import geohash

def run(latitude, longitude, datedow):
    geohash(float(latitude), float(longitude), str(datedow).encode('utf-8'))

if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 4:
        run(arg[1], arg[2], arg[3])
    else:
        print("Error: You need set 3 parameters latitude, longitude, datedow. E.g: python3 geohashing.py 37.421542 -122.085589 b'2005-05-26-10458.68'")
