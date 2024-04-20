from typing import List, Dict

class Style:
    def __init__(
            self,
            style: Dict = {}
    ):
        self.style = style
    
    def set_property(self, key: str, val: str):
        self.style.update({key: val})

    def __str__(self):
        return ",".join([f"{k}:{v}" for k, v in self.style.items()])

class StyleClass:
    def __init__(
            self,
            id: str,
            style: Style
    ):
        self.id = id
        self.style = style
    
    def __str__(self):
        return f"classDef {self.id} {self.style}"
