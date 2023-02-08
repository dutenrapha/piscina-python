import sys
import os

def doctype():
    return '''    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        {placeholder}
    </body>
    </html>'''

def insert_placeholder(base_html, placeholder, new_html):
    resp = base_html.replace(placeholder,new_html)
    return resp

def generate_html(html, html_name):
    file_html = open(f"{html_name}.html", "w")
    file_html.write(html)
    file_html.close()

def run(arg):
    with open(arg, "r") as my_file:
        template = my_file.read()
        html = insert_placeholder(doctype(), "{placeholder}", template)
        for k, v in d.items():
            html = insert_placeholder(html, "{" + str(k) + "}", str(v))
        generate_html(html, arg.split(".")[0])

def is_valide_file(arg):
    _, file_extension = os.path.splitext(arg)
    if file_extension == ".template":
        return True
    else:
        return False

def temp(**kwargs):
  return kwargs

if __name__ == '__main__':
    arg = sys.argv    
    var = open("./settings.py").read()
    var = var.replace("\n", ",")
    exec(f"d = temp({var})")
    if len(arg) == 2: 
        if is_valide_file(arg[1]):
            run(arg[1])
        else:
            print("Invalid template file. You need pass a file with templete extension. E.g. python3 render.py file.template")
    else:
        print("Error: you need call just one template file. E.g. python3 render.py file.template")
