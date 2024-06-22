import hashlib
class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        
class HashRing:
    def __init__(self, nodes, replicas=100):
        self.nodes = nodes
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []
        
        for node in nodes:
            for i in range(replicas):
                key = self.get_key(node.id, i)
                self.ring[key] = node
                self.sorted_keys.append(key)
                
        self.sorted_keys.sort()
        
    def get_key(self, node_id, i):
        return int(hashlib.md5(("%s:%s" % (node_id, i)).encode('utf-8')).hexdigest(), 16)
        
    def get_node(self, data):
        key = int(hashlib.md5(data.encode('utf-8')).hexdigest(), 16)
        for i in range(len(self.sorted_keys)):
            node_key = self.sorted_keys[i]
            if node_key >= key:
                return self.ring[node_key].data
                
        return self.ring[self.sorted_keys[0]].data
        
nodes = [Node("Node %d" % i, "192.168.1.%d" % i) for i in range(10)]
print("Node %d" % 1)
for node in nodes:
    print(node.id, node.data)
hash_ring = HashRing(nodes)
print(int(hashlib.md5(("0:0").encode('utf-8')).hexdigest(),16))
data = "Hello, World!"
node = hash_ring.get_node(data)
print("Data:", data)
print("Node:", node)
