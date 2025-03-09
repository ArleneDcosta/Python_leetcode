
class TreeNode():
    def __init__(self,val , parent=None):
        self.val = val
        self.parent = parent
        self.children = {}

class TreeOperation():
    def __init__(self):
        self.rootlist = []

    def get_no_of_root(self,generated):
        rootlist = []
        for _,node in generated.items():
            if node.parent is None:
                rootlist.append(node)

        self.rootlist = rootlist
        return rootlist
    
    def get_tree_count(self,root):
        count = 0
        queue = [root]
        while len(queue) != 0:
            currentnode = queue.pop()
            count += 1
            for child in currentnode.children:
                queue.append(currentnode.children[child])

        return count
    
    def get_max_node_tree(self):
        result = {}
        for root in self.rootlist:
            result[root] = self.get_tree_count(root)
        maxval = -1000
        maxnode = None
        for node,count in result.items():
            if count > maxval:
                maxval = count
                maxnode = node

        return maxnode

if __name__ == '__main__':
    immediateParent = {2: 1,3: 1,4: 2,5: 2,6: 3,8: 7,9: 7,10: 9}
    generated = {}
    for childval, parentval in immediateParent.items():
        if parentval not in generated:
            parentnode = TreeNode(parentval)
            generated[parentval] = parentnode
        else:
            parentnode = generated[parentval]

        if childval not in generated:
            childnode = TreeNode(childval)
            generated[childval] = childnode

        else:
            childnode = generated[childval]
        

        parentnode.children[childval] = childnode
        childnode.parent = parentnode

    t = TreeOperation()

    rootlist = t.get_no_of_root(generated)
    # print(len(rootlist))

    rootresult = t.get_max_node_tree()
    if rootresult is not None:
        print(rootresult.val)
    