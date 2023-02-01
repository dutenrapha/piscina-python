def sort_name(d):
    for k in d.keys():
        d[k].sort()
    sorted_by_key = dict(sorted(d.items()))
    return(sorted_by_key)

def invert_dict(d):
    resp = {}
    for k,v in d.items():
        if v in resp.keys():
            resp[v].append(k)
        else:
            resp[v] = [k]
    return resp
    
def run():
    d = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',
    'Beck' : '1944',
    'Santana' : '1947',
    'Ramone' : '1948',
    'White' : '1975',
    'Frusciante': '1970',
    'Thompson' : '1949',
    'Burton' : '1939',
    }
    resp = invert_dict(d)
    resp = sort_name(resp)
    for musicians in resp.values():
        for musician in musicians:
            print(musician)

if __name__ == '__main__':
    run()