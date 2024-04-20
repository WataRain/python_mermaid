from typing import List, Optional
from .node import AbstractNode, Node
from .link import Link
from .interaction import Interaction
from .style_class import Style, StyleClass

DIAGRAM_TYPES = {
    "default": "graph",
    "flowchart": "flowchart",
    "statechart": "stateDiagram-v2"
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
        interactions: List[Interaction] = [],
        style_classes: List[StyleClass] = [],
        type="default",
        orientation="default"
    ):
        self.title = title
        self.nodes = nodes
        self.links = links
        self.interactions = interactions
        self.style_classes = style_classes
        self.type = DIAGRAM_TYPES[type]
        self.orientation = DIAGRAM_ORIENTATION[orientation]
        self.startNode = None
        self.endNode = None

    def add_nodes(self, nodes=[]):
        self.nodes += nodes

    def add_links(self, links=[]):
        self.links += links

    def add_style_class(self, style_class=[]):
        self.style_classes += style_class

    def add_start_and_end_nodes(self, 
                                start_node:Optional[AbstractNode] = None, 
                                end_node:Optional[AbstractNode] = None):
        self.startNode = start_node # type: ignore
        self.endNode = end_node # type: ignore

    def __get_graph_str(self):
        style_classes_string = (
            '\n'.join([str(style_class) for style_class in self.style_classes])
        )
        nodes_string = (
            '\n'.join([str(node) for node in self.nodes])
        )
        links_string = (
            '\n'.join([str(link) for link in self.links])
        )
        interactions_string = (
            '\n'.join([str(interaction) for interaction in self.interactions])
        )
        final_strings = list(
            filter(
                None,
                [
                    f"{self.type} {self.orientation}",
                    style_classes_string,
                    nodes_string,
                    links_string,
                    interactions_string
                ]
            )
        )
        return '\n'.join(final_strings)
    
    def __get_state_diagram_str(self):
        style_classes_string = (
            '\n'.join([str(style_class) for style_class in self.style_classes])
        )
        nodes_string = (
            '\n'.join([str(node) for node in self.nodes if str(node)!=""])
        )
        links_string = (
            '\n'.join([str(link) for link in self.links])
        )
        final_strings = list(
            filter(
                None,
                [
                    f"{self.type}",
                    style_classes_string,
                    nodes_string,
                    f"[*] --> {self.startNode.id}" if self.startNode else None,
                    links_string,
                    f"{self.endNode.id} --> [*]" if self.endNode else None
                ]
            )
        )
        return '\n'.join(final_strings)

    def __str__(self):
        self.string = f"---\ntitle: {self.title}\n---\n" if self.title else ""
        content = ""
        if self.type == "graph":
            content = self.__get_graph_str()
        elif self.type == "stateDiagram-v2":
            content = self.__get_state_diagram_str()
        self.string += content
        return self.string
        
