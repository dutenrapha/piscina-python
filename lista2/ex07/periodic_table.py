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

def html_box_full():
    return '''<td style="border: 1px solid black; padding:10px">
                    <h4>Hydrogen</h4>
                    <ul>
                        <li>No 42</li>
                        <li>H</li>
                        <li>1.00794</li>
                        <li>1 electron</li>
                    <ul>
                </td>'''

def html_table():
    return '''<table>
            <tr>
                {{box}}
                {{box}}
                {{box_empty}}
                {{box_empty}}
                {{box}}
            </tr>
            <tr>
                {{box}}
                {{box_empty}}
                {{box_empty}}
                {{box}}
                {{box}}
            </tr>
            <tr>
                {{box}}
                {{box_empty}}
                {{box}}
            </tr>
        </table>'''


def read_txt():
    with open('periodic_table.txt') as f:
        numbers = f.readlines()
        numbers = numbers[0].split(",")
        for number in numbers:
            print(number)

def generate_html(html):
    file_html = open("periodic_table.html", "w")
    file_html.write(html)
    file_html.close()

if __name__ == '__main__':
    read_txt()
    html_t = insert_placeholder(html_table(), "{{box}}", html_box_full())
    html_t = insert_placeholder(html_t, "{{box_empty}}", html_box_empty())
    html = insert_placeholder(doctype(), "{{placeholder}}", html_t)
    generate_html(html)