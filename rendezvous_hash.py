
from bitarray import bitarray
from pickle_hash import hash_code_hex
import pickle
import hashlib
import math


class RendezvousHash():
    def __init__(self, weights, seeds):
        self.weights = weights
        self.seeds = seeds

    def compute_score(self, key, i):
        key_bytes = key.encode()
        hash = hashlib.md5(self.seeds[i].encode() + key_bytes).hexdigest()
        hash_float = float(int(hash, 16))
        print("compute_score()------ hash_float: ", hash_float)
        score = 1.0 / math.log(hash_float)
        print("compute_score()------ score: ", score)
        return score * self.weights[i]

    def get_node(self, key, node_ring):
        print("RedezvousHash(): ", node_ring)
        highest_score, targer_node_position, i = -1, -1, 0
        for node in node_ring:
            score = self.compute_score(key, i)
            if score > highest_score:
                highest_score, targer_node_position = score, i
            i += 1

        print("get_node()---targer_node_position: ", targer_node_position)
        return targer_node_position
