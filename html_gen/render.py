from html_gen.core import Element, Text

def parse(target, level = 0, output = None):

    if output is None:
        output = []

    if isinstance(target, Text):
        if level < 0:
            output.pop()
            output.pop()
        output.append(target.text)
        if level > 0: output.append("\n")
        return

    tag = type(target).__name__.lower()

    if not level and tag == "html": output.extend(["<!DOCTYPE html>", "\n", "\n"])

    output.append(f"<{tag}")

    for name, value in sorted(target.attributes.items()):
        output.append(f' {name}="{value}"')

    output.extend([">", "\n"])

    if tag == "html": output.append("\n")

    if target.self_closing: return

    only_content = all(isinstance(child, Text) for child in target.children)

    for child in target.children:
        output.append(" " *  (level + 1) * 4)
        if only_content: parse(child, -level - 1, output)
        else: parse(child, level + 1, output)
        if isinstance(child, Element) and not child.self_closing:
            output.append("\n")

    if not only_content: output.append(" " * level * 4)

    if tag == "html": output.append("\n")

    output.append(f"</{tag}>")

    if tag == "head": output.append("\n")

    if not level: return "".join(output) + "\n"
    
def flat_parse(target, output = None):

    if output is None:
        output = []

    if isinstance(target, Text):
        output.append(target.text)
        return

    tag = type(target).__name__.lower()

    output.append(f"<{tag}")

    for name, value in sorted(target.attributes.items()):
        output.append(f' {name}="{value}"')

    output.extend([">"])

    if target.self_closing: return

    only_content = all(isinstance(child, Text) for child in target.children)

    for child in target.children:
        if only_content: flat_parse(child, output)
        else: flat_parse(child, output)

    output.append(f"</{tag}>")

    return "".join(output)
