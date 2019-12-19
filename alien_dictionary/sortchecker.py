from typing import List
from itertools import zip_longest

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet_map = {}
        alphabet_map[None] = -1
        for index, letter in enumerate(order):
            alphabet_map[letter] = index

        for i in range(1, len(words)):
            first_word = words[i-1]
            second_word = words[i]
            in_order = self.pair_ordered(first_word, second_word, alphabet_map)
            if not in_order:
                return False

        return True

    def pair_ordered(self, word1, word2, alphabet_map):
        for letter1, letter2 in zip_longest(word1, word2):
            letter1_index = alphabet_map[letter1]
            letter2_index = alphabet_map[letter2]
            if letter1_index < letter2_index:
                return True
            elif letter1_index > letter2_index:
                return False

        return True

