from html_gen.core import Text, Element
from html_gen.tags import P
from html_gen.render import flat_parse
import html_gen.comparators

from re import split

class Component:


    def __init__(self):

        self.cached_format = ""

    def __call__(self, elements:dict):

        from html_gen.cache import add_component, get_component
        add_component(self)
        
        if (cached_item := get_component(self)):
            
            cached_item = split("(\(:|:\))+", cached_item)
            
            for i in cached_item:
                if i == "(:":
                    if (argument := cached_item[(index := cached_item.index(i))+1].split())[0] == "if":
                        if (comparator := argument[2]) == "==":
                            compare = html_gen.comparators.eq
                        elif (comparator := argument[2]) == "!=":
                            compare = html_gen.comparators.noteq
                            
                        if compare(elements[argument[1]], argument[3].replace("_", " ")):
                            cached_item[index:index+3] = ""
                            cached_item[index+1:index+4] = ""
                        else:
                            cached_item[index: index+7] = ""
            
            cached_item = "".join(cached_item)
            
            return Text(cached_item.format(**elements))
        
    def add(self, tag, update:bool=False, textvar:str=None, children:list[Element]=None, parts:list[str]=None) -> str:

        cached_format = ""
        cached_format += f"<{tag}>"
        
        if textvar:
            cached_format += f"{{{textvar}}}"
        if children:
            for child in children:
                cached_format += flat_parse(child)
        if parts:
            for part in parts:
                cached_format += part
        cached_format += f"</{tag}>"
        
        if update is True:
            self.cached_format = cached_format
        
        return cached_format
    
    def add_if(self, statement:str, parts:str=None) -> str:
        
        statement_ = f"(: if {statement} :)"
        if parts:
            for part in parts:
                statement_ += part
        statement_ += "(: /if :)"
        
        return statement_
        