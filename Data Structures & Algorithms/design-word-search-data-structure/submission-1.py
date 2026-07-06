class TriNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TriNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
              curr.children[c] = TriNode()
        
            curr = curr.children[c]

        curr.eow = True


    def search(self, word: str) -> bool:


        def dfs(j,root):
            curr = root

            for i in range(j,len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.eow
        return dfs(0, self.root)
        
        


