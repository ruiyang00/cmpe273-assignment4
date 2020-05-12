from hashlib import md5
from bisect import bisect
from node_ring import NodeRing
from server_config import NODES
import pprint


class ConsistentHash():
    def __init__(self, physical_ring, vnodes_factor=2):
        self.num_replicas = vnodes_factor
        self.vnodes = self.generate_virtual_ring(physical_ring, vnodes_factor)
        self.vnodes_hash, self.vnodes_hash_map = self.generate_vnodes_hash(
            physical_ring)

        print(self.vnodes_hash)

    def generate_vnodes_hash(self, nodes):
        print(nodes)
        salt = ["cmpe", "273"]
        hash = []
        map = {}

        for i in range(len(salt)):
            print("i", i)
            for node in nodes:
                salted = (str(node)+salt[i])
                digest = md5((str(node)+salt[i]).encode())
                h = int(digest.hexdigest(), 16)
                hash.append(h)
                map[h] = nodes.index(node)

        hash.sort()
        return hash, map

    @staticmethod
    def generate_virtual_ring(physical_ring, vnodes_factor):
        nodes = []
        for i in range(vnodes_factor):
            for node in physical_ring:
                nodes.append(node)
        return nodes

    def get_node(self, key):
        key_str = md5(key.encode()).hexdigest()
        k = int(key_str, 16)
        position = bisect(self.vnodes_hash, k)

        if position == len(self.vnodes_hash):
            return self.vnodes_hash_map[self.vnodes_hash[0]]
        else:
            return self.vnodes_hash_map[self.vnodes_hash[position]]


# clients = [
#     UDPClient(server['host'], server['port'])
#     for server in NODES
# ]
# ring = NodeRing(clients)
# virtual_ring = ConsistentHash(NODES)


# print(virtual_ring)


# physical_ring.apply_new_hash(virtual_ring)
