from click import argument
from html_gen.render import flat_parse, parse
from html_gen.tags import Body, Button, H3, Head, Html, Img, Link, P
from html_gen.component import Component
from html_gen.cache import add_component, Cache

test = Component()

test.add(tag="h1", update=True, 
         parts=test.add_if(statement="hello == 'good morning'", 
                           parts=test.add(tag="p", textvar="hello"), ))
add_component(test)

page = Html(
    Head(Link(attributes={"href": "https://google.com/favicon.ico"})),
    Body(
        H3("This is a header", attributes={"align": "center"}),
        test(elements={"hello":"good morning"}),
        Img(attributes={"src": "https://google.com"}),
        P("This is a paragraph.", Button("Hi!"))
    ),
    attributes={"lang": "en"}
)

print(Cache)

print(parse(page))