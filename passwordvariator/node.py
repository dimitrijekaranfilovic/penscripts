from typing import Callable
from copy import deepcopy

def get_leaves(root: 'Node', leaves: list['Node'] = None) -> list['Node']:
    if root is None:
        return []
    if leaves is None:
        leaves = []
    if len(root.children) == 0:
        leaves.append(root)
        return
    else:
        for child in root.children:
            get_leaves(child, leaves)
    return leaves


class Node:
    def __init__(self,
                 *, 
                 children: list['Node'] = None,
                 state: list[str] = None) -> None:
        self.children: list['Node'] = children or []
        self.__state: list[str] = state or []

    def add_children(self, index: int, transformations: list[Callable[[str], str]]):
        for transformation in transformations:
            new_state = deepcopy(self.__state)
            new_char = transformation(new_state[index])
            if new_state[index] == new_char:
                continue
            new_state[index] = new_char
            self.children.append(Node(state=new_state))

    def get_str_state(self):
        return ''.join(self.__state)
    
    def add_child(self, child: 'Node'):
        self.children.append(child)
