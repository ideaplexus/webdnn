from typing import Callable

from webdnn.graph import node
from webdnn.graph.attribute import Attribute
from webdnn.graph.operators.attributes.inplace import Inplace


class InlineInplace(Attribute):
    injector: Callable[[str], str]
    inplace: Inplace

    def __init__(self, base: "node.Node", injector: Callable[[str], str], inplace: Inplace):
        super(InlineInplace, self).__init__(base)
        self.injector = injector
        self.inplace = inplace

    def get_input(self):
        return self.inplace.get_input()

    def get_output(self):
        return self.inplace.get_output()


class PostInlineInplace(Attribute):
    injected: InlineInplace = None

    def register_injected(self, attr: InlineInplace):
        self.injected = attr
