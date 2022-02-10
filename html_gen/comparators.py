def parse_comparator(comparator:str):
    
    if comparator == "==":
        return eq
    elif comparator == "!=":
        return noteq

def parse_variable(var:str, elements:dict[str:str]):
    
    if var.startswith("'") and var.endswith("'"):
        pass
    else:
        try:
            var = int(var)
        except:
            var = elements[var]
    return var

def eq(a, b):
    
    if a == b:
        return True
    return
    
def noteq(a, b):
    
    if a != b:
        return True
    return
    
def lt(a, b):
    
    if a < b:
        return True
    return
    
def gt(a, b):
    
    if a > b:
        return True
    return
    
def lteq(a, b):
    
    if a <= b:
        return True
    return

def gteq(a, b):
    
    if a >= b:
        return True