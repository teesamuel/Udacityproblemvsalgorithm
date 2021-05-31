class TrieNode():
    def __init__(self,char=''):
        self.character=char
        self.children={}
        self.is_last=False

    def add(self, char):
        if char not in self.children:
            # self.children.append(char) 
            self.children[char]='' 
            self.character = char
        else:
            return   

    def suffixes(self,input):
        node=self
        # check if node is empty
        string_list=list(input)
        if not node.children or len(string_list)==0  or string_list[0] not in node.children:
            return -1

        for ch in string_list:
            word_exist=False
            if ch in node.children:
                node=node.children[ch]
                word_exist=True
        if not word_exist:
                return []
        else:
            # print(node.character)
            return self.list_of_words(node)
    
    def list_of_words(self,trie):
  
        output_list = []
        for k, v in trie.children.items():
            if v.is_last is not True:
                for el in self.list_of_words(v):
                    output_list.append(k + el)
            else:
                if v.children:
                    for el in self.list_of_words(v):
                        output_list.append(k + el)
                output_list.append(k)

        return output_list


class Trie():
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                new_node=TrieNode(char)
                node.children[char]=new_node
            node = node.children[char]

        node.is_last=True
        return self.root
    def find_a_word(self,word):
        if len(word)==0 or str(word)=='':
            return False
        if word not in self.root.children:
            return False
        return self.root.children[word]
          
MyTrie = Trie()

wordList = [
    "ant", "anthology", "animal","any","antagonist", "antonym",
    "fun", "function","functions","tree","funny", "factory",
    "trie", "trigger", "trigonometry", "trinity"
]

for word in wordList:
    MyTrie.insert(word)

print(MyTrie.root.children['a'].character) #a
print(MyTrie.find_a_word('')) #False
print(MyTrie.find_a_word('p'))  #False
print(MyTrie.root.suffixes('a'))  #['nthology', 'ntagonist', 'ntonym', 'nt', 'nimal', 'ny']
print(MyTrie.root.suffixes('fun')) #['ctions', 'ction', 'ny']
print(MyTrie.root.suffixes('tr')) #['ee', 'ie', 'igger', 'igonometry', 'ipod']
print(MyTrie.root.suffixes('')) #-1