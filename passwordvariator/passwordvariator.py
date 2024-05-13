import argparse
import itertools
from random import choice
from typing import Callable
from node import Node,  get_leaves

substitions = {
    'a': ['@', '4'],
    'b': ['8', 'I3', '13', '!3'],
    'c': ['[', '<'],
    'd': [')', '|)'],
    'e': ['3', '&', '€'],
    'f': ['|'],
    'g': ['6', '9'],
    'h': ['#'],
    'i': ['1', '|'],
    'j': ['_|', ',_|'],
    'k': ['>|', '|<'],
    'l': ['1', '7'],
    'o': ['0', '()'],
    's': ['5'],
    't': ['7'],
    'x': ['><'],
    'y': ['j'],
    'z': ['2'],
    '@': ['a'],
    '4': ['a'],
    '8': ['b'],
    '6': ['g'],
    '[': ['c'],
    '2': ['z'],
    '0': ['o'],
    '1': ['i'],
}

special_characters_and_numbers = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', ',', '<', '>', '/', '\\', 
    '?', '_', '-', '=', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]

def uppercase(c: str) -> str:
    return c.upper()

def lower(c: str) -> str:
    return c.lower()

def substitute(c: str) -> str:
    s = substitions.get(c.lower())
    return choice(s) if s else c

per_letter_transformations: list[Callable[[str], str]] = [uppercase, lower, substitute]

def combine(keyword: str, results: list[str]):
    keyword_len = len(keyword)
    keyword_range = range(keyword_len)
    for i in range(1, keyword_len + 1):
        # perform transformations on i characters of the word the word each iteration
        # list of tuples, where each tuple contains indices of characters to be transformed
        indices_to_transform = list(itertools.combinations(keyword_range, i))
        for indices in indices_to_transform:
            # for each combination of indices, do separate transformations
            # new_word = list(keyword)
            root = Node(state=list(keyword))
            candidates = [root]
            for index in indices:
                for candidate in candidates:
                    candidate.add_children(index, per_letter_transformations)
                candidates = get_leaves(root)
            leaves = get_leaves(root)
            for leaf in leaves:
                state = leaf.get_str_state()
                if state == keyword:
                    continue
                results.append(state)
    return results


def add_special_characters_and_numbers(keyword: str, results: list[str]):
    n = len(special_characters_and_numbers)
    n_range = range(n)
    final_to_add = []
    for i in range(1, 4):
        special_characters_to_add = list(itertools.combinations(n_range, i))
        for t in special_characters_to_add:
            to_add = ''.join([special_characters_and_numbers[i] for i in t])
            final_to_add.append(to_add)
    
    with_special_characters = []

    for to_add in final_to_add:
        for r in results:
            with_special_characters.append(to_add + r)
            with_special_characters.append(r + to_add)
    results.extend(with_special_characters)   
    return results

def main(keyword: str):
    results = [keyword]
    combine(keyword, results)
    add_special_characters_and_numbers(keyword, results)
    print('\n'.join(set(results)))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='passwordvariator.py',
                                     description='Creates a list of variations of the keyword')

    parser.add_argument('keyword', help='Keyword')
    args = parser.parse_args()
    main(args.keyword)