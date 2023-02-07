import elem

class Html(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content)

class Head(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content)

class Body(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content)

class Title(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content)

class Meta(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='meta', attr=attr, tag_type='simple')

class Img(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='img', attr=attr, tag_type='simple')

class Table(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content)

class Th(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content)

class Tr(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content)

class Td(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content)

class Ul(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content)

class Ol(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content)

class Li(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content)

class H1(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content)

class H2(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content)

class P(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content)

class Div(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', attr=attr, content=content)

class Span(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content)

class Hr(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='hr', attr=attr, tag_type='simple')

class Br(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', attr=attr, tag_type='simple')

if __name__ == '__main__':
    #print( Html( [
    #   Head(), 
    #   Body()] ) )
    # 
    # 
    #print( Html( [Head(), Body([H1(elem.Text("Isso é um H1!")),H2(elem.Text("Isso é um H2!")),Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])])) 
    
    # print( Html( 
    #     [Head([
    #         Title(elem.Text("Helo Ground!"))]), 
    #     Body([
    #         H1(elem.Text("Oh no, not again!")),
    #         Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])]))
    
    print(Html([Head(), Body()])) 