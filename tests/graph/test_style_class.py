from python_mermaid.node import Node
from python_mermaid.style_class import Style, StyleClass
from python_mermaid.diagram import MermaidDiagram

def test_style_class():
    style = Style({"stroke": "#f00"})
    style_class = StyleClass("sample_style", style)
    node = Node("Hi", style=style)
    node2 = Node("Hi 2", style_class=style_class)
    m = MermaidDiagram(title = "Hello", nodes=[node, node2], style_classes=[style_class])
    print(m)
