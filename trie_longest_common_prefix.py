from collections import defaultdict, deque
from typing import *


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.common_prefix = ""

    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def find_longest_prefix(self):
        node = self.root

        queue = deque([node])

        while queue:
            curr = queue.popleft()

            if not len(curr.children) == 1:
                break
            else:
                for c in curr.children:
                    queue.append(curr.children[c])
                    self.common_prefix += c
                    if curr.children[c].is_word:
                        return self.common_prefix

        return self.common_prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            if not word:
                return ""
            trie.insert(word)

        return trie.find_longest_prefix()


strs = ["flower","flow","flight", "fly", "fling", "flown"]
res = Solution().longestCommonPrefix(strs)
print(res)

strs = ["dog","racecar","car"]
res = Solution().longestCommonPrefix(strs)
print(res)

strs = ["","b"]
res = Solution().longestCommonPrefix(strs)
print(res)

strs = ["ab", "a"]
res = Solution().longestCommonPrefix(strs)
print(res)
