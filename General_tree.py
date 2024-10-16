class treeNode:
    def __init__(self, data):
        self.data = data
        self.children  = []
        self.parent = None

    def add_child(self,child):
        child.parent =  self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = "-" * self.get_level()*2
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
                
if __name__=="__main__":
    root = treeNode("A")
    b = treeNode("B")
    c=treeNode("C")
    root.add_child(b)
    root.add_child(c)

    d = treeNode("D")
    e = treeNode("E")
    b.add_child(d)
    b.add_child(e)
    
    root.print_tree()


