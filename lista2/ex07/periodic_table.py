import sys

def doctype():
    return '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        placeholder
    </body>
    </html>'''

def insert_placeholder(base_html, placeholder, new_html):
    resp = base_html.replace(placeholder,new_html)
    return resp

def html_box_empty():
    return '''<td style="border: 1px solid black; padding:10px">
      
                </td>'''

def html_box_full(name, number, small, molar, electron):
    return f"<td style=\"border: 1px solid black; padding:10px\"><h4>{name}</h4><ul><li>No {number}</li><li>{small}</li><li>{molar}</li><li>{electron}</li><ul></td>"

def html_table(rows, columns):
    base = '''<table>
            placeholder
        </table>'''
    r = ""
    for row in range(rows):
        r = r  + f"<tr> row_{row} </tr>"
    base = insert_placeholder(base, "placeholder", r)
    for row in range(rows):
        c = ""
        for column in range(columns):
                c = c + f"row_{row}_{column} "
        base = insert_placeholder(base, f"row_{row}", c)
    return(base)

def extract(str, tpy="key"):
    if tpy == "key":
        return(str.split("=")[0].strip())
    elif tpy == "position":
        return(int(str.split(":")[1].strip()))
    elif tpy == "value":
        return(str.split(":")[1])
    else:
        return(None)

def read_txt():
    d = {}
    with open('periodic_table.txt') as f:
        lines = f.readlines()
        for line in lines:
            l = line.strip()
            l = l.split(",")
            d[extract(l[0])] = {"position": extract(l[0], "position"),
                                "number": extract(l[1], "value"),
                                "small": extract(l[2], "value"),
                                "molar": extract(l[3], "value"),
                                "electron": extract(l[4], "value")}
    return(d)

def generate_html(html):
    file_html = open("periodic_table.html", "w")
    file_html.write(html)
    file_html.close()

if __name__ == '__main__':
    d = read_txt()
    row = 0
    html = html_table(7,18)
    for k, v in d.items():
        print(f"row_{row}_{v['position']}")
        html_box = html_box_full(name=k, number=v['number'], small=v['small'], molar=v['molar'], electron=v['electron'])
        temp = insert_placeholder(html, f"row_{row}_{v['position']}", html_box)
        html = temp

        if v['position'] == 17:
            row += 1
        
    
    html = insert_placeholder(doctype(), "placeholder", html)
    generate_html(html)