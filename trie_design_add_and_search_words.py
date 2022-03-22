from collections import defaultdict, deque
from typing import *


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.common_prefix = ""
        self.cache = {}

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

        self.cache[word] = {}

    def search(self, word: str) -> bool:
        if not word in self.cache:
            self.cache[word] = self.dfs(self.root, word)
        return self.cache[word]

    def dfs(self, node, word):
        if not word and node.is_word:
            return True

        if not node:
            return False

        for idx, c in enumerate(word):
            if c == ".":
                for child in node.children:
                    curr = child + word[idx + 1 :]
                    if self.dfs(node, curr):
                        return True
            if c in node.children:
                return self.dfs(node.children[c], word[idx + 1 :])
            else:
                return False

        return False

# wordDictionary = WordDictionary()
# words = ["bad", "dad", "mad"]
# for w in words:
#     wordDictionary.addWord(w)
#
# print("Words registered: ", words)
#
# word = "pad"
# res = wordDictionary.search(word)
# print(word)
# print(res)
#
# word = "bad"
# res = wordDictionary.search(word)
# print(word)
# print(res)
#
# word = "pad"
# wordDictionary.addWord("pad")
# res = wordDictionary.search(word)
# print(word)
# print(res)
#
# word = ".ad"
# res = wordDictionary.search(word)
# print(word)
# print(res)
#
# word = "b.."
# res = wordDictionary.search(word)
# print(word)
# print(res)

########################################################
wordDictionary = WordDictionary()
words = ["at", "and", "an", "add"]
for w in words:
    wordDictionary.addWord(w)

print("Words registered: ", words)

word = "a"
res = wordDictionary.search(word)
print(word)
print("Output:   ", res)
print("Expected: ", False)

word = ".at"
res = wordDictionary.search(word)
print(word)
print("Output:   ", res)
print("Expected: ", False)

w = "bat"
wordDictionary.addWord(w)
print("Words registered: ", words + [w])

word = ".at"
res = wordDictionary.search(word)
print(word)
print("Output:   ", res)
print("Expected: ", True)

word = "an."
res = wordDictionary.search(word)
print(word)
print("Output:   ", res)
print("Expected: ", True)

word = "a.d."
res = wordDictionary.search(word)
print(word)
print("Output:   ", res)
print("Expected: ", False)

word = "b."
res = wordDictionary.search(word)
print(word)
print("Output:   ", res)
print("Expected: ", False)

word = "a.d"
res = wordDictionary.search(word)
print(word)
print("Output:   ", res)
print("Expected: ", True)

word = "."
res = wordDictionary.search(word)
print(word)
print("Output:   ", res)
print("Expected: ", False)


