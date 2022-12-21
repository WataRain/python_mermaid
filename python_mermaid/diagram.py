from typing import List
from .node import Node
from .link import Link

DIAGRAM_TYPES = {
    "default": "graph",
    "flowchart": "flowchart"
}

DIAGRAM_ORIENTATION = {
    "default": "",
    "top to bottom": "TB",
    "top-down": "TD",
    "bottom to top": "BT",
    "right to left": "RL",
    "left to right": "LR",
}


class MermaidDiagram:
    def __init__(
        self,
        title: str = "",
        nodes: List[Node] = [],
        links: List[Link] = [],
        type="default",
        orientation="default"
    ):
        self.title = title
        self.nodes = nodes
        self.links = links
        self.type = DIAGRAM_TYPES[type]
        self.orientation = DIAGRAM_ORIENTATION[orientation]

    def add_nodes(self, nodes=[]):
        self.nodes += nodes

    def add_links(self, links=[]):
        self.links += links

    def __str__(self):
        self.string = f"---\ntitle: {self.title}\n---\n"
        nodes_string = (
            '\n'.join([str(node) for node in self.nodes])
            if len(self.nodes)
            else ''
        )
        links_string = (
            '\n'.join([str(link) for link in self.links])
            if len(self.links)
            else ''
        )
        self.string += (
            f"{self.type} {self.orientation}\n{nodes_string}\n{links_string}"
        )
        return self.string
