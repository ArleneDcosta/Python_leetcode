class Trie:
    def __init__(self):
        self.wordset = set()
        self.prefix = {}
    
    def insert(self, word: str) -> None:
        self.wordset.add(word)
        for i in range(1,len(word)+1):
            currword = word[0:i]
            if currword not in self.prefix:
                self.prefix[currword] = [word]
            else:
                self.prefix[currword].append(word)

    def search(self, word: str) -> bool:
        if word in self.wordset:
            return True
        return False
    
    def starts_with(self, prefix: str) -> bool:
        if prefix in self.prefix:
            return True
        return False
######################## SImiliar to FileSystem
class TrieNodeOpt:
        # Initialize your data structure here.
        def __init__(self):
            self.word=False
            self.children={}
    
class TrieOpt:
    
        def __init__(self):
            self.root = TrieNodeOpt()
    
        # @param {string} word
        # @return {void}
        # Inserts a word into the trie.
        def insert(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    node.children[i]=TrieNodeOpt()
                node=node.children[i]
            node.word=True
    
        # @param {string} word
        # @return {boolean}
        # Returns if the word is in the trie.
        def search(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    return False
                node=node.children[i]
            return node.word
    
        # @param {string} prefix
        # @return {boolean}
        # Returns if there is any word in the trie
        # that starts with the given prefix.
        def startsWith(self, prefix):
            node=self.root
            for i in prefix:
                if i not in node.children:
                    return False
                node=node.children[i]
            return True
            
    
    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")

if __name__ == '__main__':
    obj = Trie()

    obj.insert("apple")
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.starts_with("app"))
    obj.insert("app")
    print(obj.search("app"))