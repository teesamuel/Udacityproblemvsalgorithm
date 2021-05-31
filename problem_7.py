# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, name):
        self.root=RouteTrieNode()
        self.name=name

    def insert(self, path,handler_name):
        splith_path=path.split('/')
        node=self.root

        for char in splith_path:
            if char not in node.children:
                node.children[char]=RouteTrieNode()
                node.character=char
                if char == splith_path[len(splith_path)-1]:
                    node.handler=handler_name
                    break
            node=node.children[char]
    def find(self,path):
        current_node=self.root
        while current_node.children:
            if path in current_node.children:
                return current_node.handler
            current_node=current_node.children[current_node.character]
        return current_node.handler

class RouteTrieNode:
    def __init__(self):
        self.handler=None
        self.children={}
        self.character=''

    def insert(self, path):
        if path not in self.children:
            self.children[path]=''
            self.character=path
        else:
            return

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, name):
        self.root=RouteTrie(name)

    def add_handler(self, path, handle_name):
        return self.root.insert(path,handle_name)

    def lookup(self, path):
        if str(path) =="/":
            return self.root.name
        split_string=path.split("/")
        last_val=split_string.pop()
        # return last_val
        return self.root.find(last_val)

    def split_path(self, path):
        string_split=path.split("/")
        return string_split

router = Router("root handler")
router.add_handler("/home/about", "about handler")
print(router.lookup("/"))
print(router.lookup("/home"))
print(router.lookup("/home/about"))
print(router.lookup("/home/about/"))
print(router.lookup("/home/about/me/"))
print(router.lookup("/home/dance"))