import hashlib
# from rendezvous_hash import rendezvous_hash
# from consistent_hash import consistent_hash


from server_config import NODES


class NodeRing():

    def __init__(self, nodes):
        assert len(nodes) > 0
        self.nodes = nodes
        self.hash_function = None

    def get_node(self, key_hex):

        print("get_node()--self.hash_fucntion: ", self.hash_function)
        if self.hash_function == None:
            key = int(key_hex, 16)
            node_index = key % len(self.nodes)

        else:
            node_index = self.hash_function.get_node(key_hex, self.nodes)

        return self.nodes[node_index]

    def apply_new_hash(self, hash):
     

        self.hash_function = hash




# def test():
#     ring = NodeRing(nodes=NODES)
#     node = ring.get_node('9ad5794ec94345c4873c4e591788743a')
#     print(ring)
#     print(ring.get_node('ed9440c442632621b608521b3f2650b8'))


# Uncomment to run the above local test via: python3 node_ring.py
# test()
