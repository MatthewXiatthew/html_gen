from html_gen import cache
from html_gen.component import Component

Cache = {}

def add_component(component):

     if isinstance(component, Component):

        Cache[id(component)] = component.cached_format
            

def get_component(component):

    if (type_ := id(component)) in Cache:
        return Cache[type_]

    else:
        return