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
        {{placeholder}}
    </body>
    </html>'''

def insert_placeholder(base_html, placeholder, new_html):
    return base_html.replace(placeholder,new_html)

def html_box_empty():
    return '''<td style="border: 1px solid black; padding:10px">
      
                </td>'''

def html_box_full(name, number, small, molar, electron):
    return f"<td style=\"border: 1px solid black; padding:10px\"><h4>{name}</h4><ul><li>No {number}</li><li>{small}</li><li>{molar}</li><li>{electron}</li><ul></td>"

def html_table(rows, columns, empty_list=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[2,3,4,5,6,7,8,9,10,11],[2,3,4,5,6,7,8,9,10,11],[],[],[],[]]):
    base = '''<table> placeholder </table>'''
    r = ""
    for row in range(rows):
        r = r + f"<tr> row_{row} </tr>"
    base = insert_placeholder(base, "placeholder", r)

    for row in range(rows):
        c = ""
        for column in range(columns):
            if column in empty_list[row]:
                c = c + " box_empty"
            else:
                c = c + f" box_{row}_{column}"
        base = insert_placeholder(base, f"row_{row}", c)
    return(base)

def read_txt():
    with open('periodic_table.txt') as f:
        lines = f.readlines()
        for line in lines:
            l = line.strip()
            l = l.split(",")
            print(l)

def generate_html(html):
    file_html = open("periodic_table.html", "w")
    file_html.write(html)
    file_html.close()

if __name__ == '__main__':
    # html = html_table(7,18)
    # html = insert_placeholder(html, "box_empty", html_box_empty())
    # for row in range(7):
    #     for column in range(18):
    #         html = insert_placeholder(html, f"box_{row}_{column}", html_box_full())
    read_txt()
    # html_t = insert_placeholder(html_table(3,10), "{{box}}", html_box_full())
    # html_t = insert_placeholder(html_t, "{{box_empty}}", html_box_empty())
    # html = insert_placeholder(doctype(), "{{placeholder}}", html_t)
    # generate_html(html)