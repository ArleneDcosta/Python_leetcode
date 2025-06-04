from typing import List
from collections import defaultdict

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences = sentences
        self.times = times
        self.tree = self.createTree(sentences)

    def createTree(self, sentences):
        tree = defaultdict(list)
        for i,sentence in enumerate(sentences):
            for j in range(1,len(sentence) + 1):
                tree[sentence[:j]].append((self.times[i],sentence))
        return tree

    def input(self,c) -> List[str]:
        result = self.tree[c]
        if len(result) == 0:
            return []
        else:
            currentresult = sorted(result,key = lambda x: (-x[0],x[1]))
            return [ val[1] for val in currentresult][:3]

class TrieNode:
    def __init__(self):
        self.children = {}  # {char: TrieNode}
        self.sentence_count = defaultdict(int)  # {sentence: count}

class AutocompleteSystemOp:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.current_input = ""
        self.curr_node = self.root  # Track where we are while typing
        
        # Insert initial sentences into Trie
        for sentence, count in zip(sentences, times):
            self.insert(sentence, count)

    def insert(self, sentence: str, count: int):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentence_count[sentence] += count

    def search(self, prefix: str) -> List[str]:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        
        # Now node.sentence_count has all sentences passing through this prefix
        sorted_sentences = sorted(node.sentence_count.items(), key=lambda x: (-x[1], x[0]))
        return [sentence for sentence, _ in sorted_sentences[:3]]

    def input(self, c: str) -> List[str]:
        if c == '#':
            # Save the whole current_input into the Trie
            self.insert(self.current_input, 1)
            # Reset
            self.current_input = ""
            self.curr_node = self.root
            return []
        
        self.current_input += c
        
        if self.curr_node and c in self.curr_node.children:
            self.curr_node = self.curr_node.children[c]
            sorted_sentences = sorted(self.curr_node.sentence_count.items(), key=lambda x: (-x[1], x[0]))
            return [sentence for sentence, _ in sorted_sentences[:3]]
        else:
            self.curr_node = None
            return []
        
        
if __name__ == '__main__':
    ac = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])

    currchar = input()
    existingstr = ""
    while (currchar != "#"):
        existingstr += currchar
        print(ac.input(existingstr))
        currchar = input()