from typing import Union

class Text:

    def __init__(self, text: str) -> None:

        self.text = text

class Element:

    self_closing = False

    def __init__(
        self, *children, attributes: dict = None
    ) -> None:

        self.attributes = attributes or {}

        self.children = []

        for child in children:
            if isinstance(child, str):
                self.append_text(child)
            else:
                self.append_element(child)

    def append_element(self, child: "Element") -> None:

        self.children.append(child)

    def append_text(self, text: str) -> None:

        self.children.append(Text(text))
