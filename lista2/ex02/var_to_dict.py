def ver_to_dict(d):
    resp = {}
    for i in d:
        if i[1] in resp.keys():
            resp[i[1]] = f"{resp[i[1]]} {i[0]}"
        else:
            resp[i[1]] = i[0]
    for key, value in resp.items():
        print(f"{key} : {value}")

def run():
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
        ]
    ver_to_dict(d)

if __name__ == '__main__':
    run()